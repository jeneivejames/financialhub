# Financial Help Hub - Supabase Setup Guide

## Step 1: Create Supabase Database Schema

1. Go to your Supabase project: https://tzrcjamabhduxezmeyze.supabase.co
2. Click on **SQL Editor** in the left sidebar
3. Click **New Query**
4. Copy the entire content from `supabase_schema.sql` file
5. Paste it into the SQL Editor
6. Click **Run** (or press Ctrl+Enter)

This will create:
- `help_requests` table (main table for storing help requests)
- `districts` table (Tamil Nadu districts reference data)
- `categories` table (Medical, Education, Emergency)
- Indexes for better performance
- Row Level Security policies for public access
- 6 sample demo requests

## Step 2: Verify Tables Created

In Supabase:
1. Click on **Table Editor** in the left sidebar
2. You should see three tables:
   - help_requests
   - districts
   - categories
3. Click on `help_requests` to see the 6 sample records

## Step 3: Set Environment Variables in Databricks App

Your Supabase credentials:
```
SUPABASE_URL=https://tzrcjamabhduxezmeyze.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR6cmNqYW1hYmhkdXhlem1leXplIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzcxMTAzMTEsImV4cCI6MjA1MjY4NjMxMX0.sb_publishable_ass8v1L806GCZFtmv81n3Q_Uh3QsnBs
```

**Note:** The SUPABASE_KEY above is your **anon/public** key (safe for client-side use).

## Step 4: Deploy the App

The app will automatically use the environment variables when deployed.

## Database Schema Overview

### help_requests table
| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key (auto-generated) |
| name | TEXT | Requester's name |
| district | TEXT | Tamil Nadu district |
| category | TEXT | Medical, Education, or Emergency |
| amount_needed | INTEGER | Amount in Rupees |
| contact | TEXT | Phone or email |
| short_description | TEXT | Brief description (100 chars) |
| detailed_message | TEXT | Full story/message |
| photo_url | TEXT | Optional photo URL |
| status | TEXT | active, closed, or fulfilled |
| created_at | TIMESTAMP | Auto-generated |
| updated_at | TIMESTAMP | Auto-updated |

### API Endpoints Created

- `GET /api/requests` - Get all help requests
- `GET /api/requests/:id` - Get single request
- `POST /api/requests` - Create new request
- `GET /api/districts` - Get all districts
- `GET /api/categories` - Get all categories
- `GET /health` - Health check

## Next Steps

1. ✅ Run the SQL schema in Supabase
2. ✅ Verify tables are created
3. ⏳ Set environment variables in the app
4. ⏳ Deploy the app
5. ⏳ Test the application

## Testing

After deployment:
1. Visit the app URL
2. You should see 6 sample requests on the home page
3. Try creating a new request through the "Need Help" form
4. The new request should appear on the home page
5. Click "View Request" to see full details

## Security Notes

- Row Level Security (RLS) is enabled
- Public read access is allowed
- Public insert is allowed for help requests
- No authentication required (public app)
- Consider adding moderation for production use

## Troubleshooting

If requests don't load:
1. Check Supabase SQL Editor for errors
2. Verify environment variables are set correctly
3. Check app logs for connection errors
4. Ensure RLS policies are created correctly