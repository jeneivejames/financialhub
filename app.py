from flask import Flask, send_file, jsonify, request
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='.')

# Initialize database connection lazily
db = None

def get_database():
    """Get or create database connection"""
    global db
    if db is None:
        try:
            from database import get_db
            db = get_db()
            logger.info("✓ Database connection established")
        except Exception as e:
            logger.error(f"✗ Database connection failed: {e}")
            logger.error(f"   Make sure SUPABASE_URL and SUPABASE_KEY are set")
            db = None
    return db

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(path):
        return send_file(path)
    return "File not found", 404

# API Endpoints
@app.route('/api/requests', methods=['GET'])
def get_requests():
    """Get all help requests"""
    try:
        db = get_database()
        if db is None:
            return jsonify({'success': False, 'error': 'Database connection failed'}), 500
        
        status = request.args.get('status', 'active')
        category = request.args.get('category')
        district = request.args.get('district')
        
        if category:
            requests = db.get_requests_by_category(category)
        elif district:
            requests = db.get_requests_by_district(district)
        else:
            requests = db.get_all_requests(status)
        
        return jsonify({'success': True, 'data': requests})
    except Exception as e:
        logger.error(f"Error in get_requests: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/requests/<request_id>', methods=['GET'])
def get_request(request_id):
    """Get a single help request by ID"""
    try:
        db = get_database()
        if db is None:
            return jsonify({'success': False, 'error': 'Database connection failed'}), 500
        
        request_data = db.get_request_by_id(request_id)
        if request_data:
            return jsonify({'success': True, 'data': request_data})
        return jsonify({'success': False, 'error': 'Request not found'}), 404
    except Exception as e:
        logger.error(f"Error in get_request: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/requests', methods=['POST'])
def create_request():
    """Create a new help request"""
    try:
        db = get_database()
        if db is None:
            return jsonify({'success': False, 'error': 'Database connection failed'}), 500
        
        data = request.json
        
        # Validate required fields
        required_fields = ['name', 'district', 'category', 'amount_needed', 'contact', 'short_description', 'detailed_message']
        for field in required_fields:
            if field not in data:
                return jsonify({'success': False, 'error': f'Missing required field: {field}'}), 400
        
        # Create the request
        new_request = db.create_request(data)
        
        if new_request:
            return jsonify({'success': True, 'data': new_request}), 201
        return jsonify({'success': False, 'error': 'Failed to create request'}), 500
    except Exception as e:
        logger.error(f"Error in create_request: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/districts', methods=['GET'])
def get_districts():
    """Get all districts"""
    try:
        db = get_database()
        if db is None:
            return jsonify({'success': False, 'error': 'Database connection failed'}), 500
        
        districts = db.get_districts()
        return jsonify({'success': True, 'data': districts})
    except Exception as e:
        logger.error(f"Error in get_districts: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get all categories"""
    try:
        db = get_database()
        if db is None:
            return jsonify({'success': False, 'error': 'Database connection failed'}), 500
        
        categories = db.get_categories()
        return jsonify({'success': True, 'data': categories})
    except Exception as e:
        logger.error(f"Error in get_categories: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    db = get_database()
    db_status = 'connected' if db else 'disconnected'
    return jsonify({
        'status': 'healthy',
        'database': db_status,
        'message': 'Financial Help Hub is running'
    }), 200

if __name__ == '__main__':
    # Use PORT environment variable (Heroku, Render, Railway, etc.) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
