import os
from supabase import create_client, Client
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

class SupabaseDB:
    def __init__(self):
        self.url = os.environ.get('SUPABASE_URL')
        self.key = os.environ.get('SUPABASE_KEY')
        
        if not self.url or not self.key:
            raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables")
        
        self.client: Client = create_client(self.url, self.key)
        logger.info(f"Connected to Supabase: {self.url}")
    
    def get_all_requests(self, status: str = 'active') -> List[Dict]:
        """Get all help requests, optionally filtered by status"""
        try:
            query = self.client.table('help_requests').select('*')
            if status:
                query = query.eq('status', status)
            
            response = query.order('created_at', desc=True).execute()
            return response.data if response.data else []
        except Exception as e:
            logger.error(f"Error fetching requests: {e}")
            return []
    
    def get_request_by_id(self, request_id: str) -> Optional[Dict]:
        """Get a single help request by ID"""
        try:
            response = self.client.table('help_requests').select('*').eq('id', request_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            logger.error(f"Error fetching request {request_id}: {e}")
            return None
    
    def create_request(self, data: Dict) -> Optional[Dict]:
        """Create a new help request"""
        try:
            response = self.client.table('help_requests').insert(data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            logger.error(f"Error creating request: {e}")
            return None
    
    def update_request(self, request_id: str, data: Dict) -> Optional[Dict]:
        """Update an existing help request"""
        try:
            response = self.client.table('help_requests').update(data).eq('id', request_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            logger.error(f"Error updating request {request_id}: {e}")
            return None
    
    def delete_request(self, request_id: str) -> bool:
        """Delete a help request"""
        try:
            self.client.table('help_requests').delete().eq('id', request_id).execute()
            return True
        except Exception as e:
            logger.error(f"Error deleting request {request_id}: {e}")
            return False
    
    def get_districts(self) -> List[Dict]:
        """Get all districts"""
        try:
            response = self.client.table('districts').select('*').order('name').execute()
            return response.data if response.data else []
        except Exception as e:
            logger.error(f"Error fetching districts: {e}")
            return []
    
    def get_categories(self) -> List[Dict]:
        """Get all categories"""
        try:
            response = self.client.table('categories').select('*').order('name').execute()
            return response.data if response.data else []
        except Exception as e:
            logger.error(f"Error fetching categories: {e}")
            return []
    
    def get_requests_by_category(self, category: str) -> List[Dict]:
        """Get help requests filtered by category"""
        try:
            response = self.client.table('help_requests').select('*').eq('category', category).eq('status', 'active').order('created_at', desc=True).execute()
            return response.data if response.data else []
        except Exception as e:
            logger.error(f"Error fetching requests by category: {e}")
            return []
    
    def get_requests_by_district(self, district: str) -> List[Dict]:
        """Get help requests filtered by district"""
        try:
            response = self.client.table('help_requests').select('*').eq('district', district).eq('status', 'active').order('created_at', desc=True).execute()
            return response.data if response.data else []
        except Exception as e:
            logger.error(f"Error fetching requests by district: {e}")
            return []

# Global database instance
db = None

def get_db() -> SupabaseDB:
    """Get or create database connection"""
    global db
    if db is None:
        db = SupabaseDB()
    return db