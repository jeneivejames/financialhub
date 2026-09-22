// Global variables
let allRequests = [];
const API_BASE = '/api';

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    loadRequests();
    setupNavigation();
    setupForm();
});

// Load all requests from database
async function loadRequests() {
    const grid = document.getElementById('requestsGrid');
    grid.innerHTML = '<p style="text-align: center; padding: 2rem;">Loading requests...</p>';
    
    try {
        const response = await fetch(`${API_BASE}/requests`);
        const result = await response.json();
        
        if (result.success && result.data) {
            allRequests = result.data;
            grid.innerHTML = '';
            
            if (allRequests.length === 0) {
                grid.innerHTML = '<p style="text-align: center; padding: 2rem;">No help requests yet. Be the first to post!</p>';
            } else {
                allRequests.forEach(request => {
                    grid.appendChild(createRequestCard(request));
                });
            }
        } else {
            grid.innerHTML = '<p style="text-align: center; padding: 2rem; color: red;">Error loading requests. Please try again.</p>';
        }
    } catch (error) {
        console.error('Error loading requests:', error);
        grid.innerHTML = '<p style="text-align: center; padding: 2rem; color: red;">Error connecting to database.</p>';
    }
}

// Create a request card element
function createRequestCard(request) {
    const card = document.createElement('div');
    card.className = 'request-card';
    
    const formattedAmount = formatCurrency(request.amount_needed);
    const imageUrl = request.photo_url || generatePlaceholderImage(request.name);
    
    card.innerHTML = `
        <img src="${imageUrl}" alt="${request.name}" class="card-image" onerror="this.src='${generatePlaceholderImage(request.name)}'">
        <div class="card-content">
            <div class="card-header">
                <div>
                    <div class="name">${request.name}</div>
                    <div class="location">${request.district}</div>
                </div>
                <span class="category">${request.category}</span>
            </div>
            <div class="amount">${formattedAmount}</div>
            <p class="message">${request.short_description}</p>
            <div class="card-actions">
                <button class="btn" onclick='viewRequest("${request.id}")'>View Request</button>
                <button class="btn btn-primary" onclick="showHelpMessage()">I Want to Help</button>
            </div>
        </div>
    `;
    
    return card;
}

// Generate placeholder image
function generatePlaceholderImage(name) {
    const colors = ['667eea', '764ba2', 'f093fb', 'f5576c', '43cea2', '5568d3'];
    const color = colors[Math.floor(Math.random() * colors.length)];
    return `data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'%3E%3Crect fill='%23${color}' width='400' height='300'/%3E%3Ctext x='50%25' y='50%25' font-size='48' fill='white' text-anchor='middle' dy='.3em'%3E${name}%3C/text%3E%3C/svg%3E`;
}

// Format currency
function formatCurrency(amount) {
    return '₹' + amount.toLocaleString('en-IN');
}

// Setup navigation
function setupNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            showSection(targetId);
            
            // Update active nav link
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

// Show specific section
function showSection(sectionId) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => section.classList.remove('active'));
    
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
    }
    
    // Update nav links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        const href = link.getAttribute('href').substring(1);
        if (href === sectionId) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Setup form submission
function setupForm() {
    const form = document.getElementById('helpRequestForm');
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(form);
        
        // Create request object
        const requestData = {
            name: formData.get('name'),
            district: formData.get('district'),
            category: formData.get('category'),
            amount_needed: parseInt(formData.get('amount')),
            short_description: formData.get('shortDesc'),
            detailed_message: formData.get('message'),
            contact: formData.get('contact'),
            status: 'active'
        };
        
        // Submit to API
        try {
            const response = await fetch(`${API_BASE}/requests`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            });
            
            const result = await response.json();
            
            if (result.success) {
                // Hide form and show success message
                document.getElementById('helpRequestForm').style.display = 'none';
                document.getElementById('formSuccess').style.display = 'block';
                document.getElementById('formSuccess').scrollIntoView({ behavior: 'smooth' });
                
                // Reload requests
                loadRequests();
            } else {
                alert('Error submitting request: ' + (result.error || 'Unknown error'));
            }
        } catch (error) {
            console.error('Error submitting request:', error);
            alert('Error submitting request. Please try again.');
        }
    });
}

// View request details
async function viewRequest(requestId) {
    const modal = document.getElementById('requestModal');
    const modalBody = document.getElementById('modalBody');
    
    // Show loading
    modalBody.innerHTML = '<p style="text-align: center; padding: 2rem;">Loading...</p>';
    modal.classList.add('active');
    
    try {
        // Try to find in cached requests first
        let request = allRequests.find(r => r.id === requestId);
        
        // If not found, fetch from API
        if (!request) {
            const response = await fetch(`${API_BASE}/requests/${requestId}`);
            const result = await response.json();
            if (result.success) {
                request = result.data;
            }
        }
        
        if (!request) {
            modalBody.innerHTML = '<p style="text-align: center; padding: 2rem; color: red;">Request not found.</p>';
            return;
        }
        
        const imageUrl = request.photo_url || generatePlaceholderImage(request.name);
        const createdDate = new Date(request.created_at).toLocaleDateString();
        
        modalBody.innerHTML = `
            <img src="${imageUrl}" alt="${request.name}" class="modal-image" onerror="this.src='${generatePlaceholderImage(request.name)}'">
            <div class="modal-header">
                <h2>${request.name}</h2>
                <p>${request.district} • ${request.category}</p>
            </div>
            <div class="modal-details">
                <p><strong>Amount Needed:</strong> ${formatCurrency(request.amount_needed)}</p>
                <p><strong>Contact:</strong> ${request.contact}</p>
                <p><strong>Posted:</strong> ${createdDate}</p>
            </div>
            <div class="modal-message">
                <p>${request.detailed_message}</p>
            </div>
            <div class="modal-actions">
                <button class="btn btn-primary" onclick="showHelpMessage()">I Want to Help</button>
                <button class="btn" onclick="closeModal()">Close</button>
            </div>
        `;
    } catch (error) {
        console.error('Error loading request:', error);
        modalBody.innerHTML = '<p style="text-align: center; padding: 2rem; color: red;">Error loading request details.</p>';
    }
}

// Close modal
function closeModal() {
    const modal = document.getElementById('requestModal');
    modal.classList.remove('active');
}

// Show help message
function showHelpMessage() {
    alert('Thank you for wanting to help!\n\nPlease contact the requester using the information provided.\n\nReminder: This is a demonstration. Please independently verify any real request before sending money.');
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('requestModal');
    if (event.target === modal) {
        closeModal();
    }
}