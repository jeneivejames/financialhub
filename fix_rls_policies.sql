-- Fix Row Level Security Policies for Financial Help Hub
-- Run this SQL in your Supabase SQL Editor to fix the 401 errors

-- Drop existing policies
DROP POLICY IF EXISTS "Allow public read access" ON help_requests;
DROP POLICY IF EXISTS "Allow public insert" ON help_requests;
DROP POLICY IF EXISTS "Allow public read on districts" ON districts;
DROP POLICY IF EXISTS "Allow public read on categories" ON categories;

-- Create new policies that explicitly allow anon role
CREATE POLICY "Public can read help requests"
ON help_requests FOR SELECT
TO anon, authenticated
USING (true);

CREATE POLICY "Public can insert help requests"
ON help_requests FOR INSERT
TO anon, authenticated
WITH CHECK (true);

CREATE POLICY "Public can read districts"
ON districts FOR SELECT
TO anon, authenticated
USING (true);

CREATE POLICY "Public can read categories"
ON categories FOR SELECT
TO anon, authenticated
USING (true);

-- Verify policies are created
SELECT schemaname, tablename, policyname, roles, cmd
FROM pg_policies
WHERE tablename IN ('help_requests', 'districts', 'categories');
