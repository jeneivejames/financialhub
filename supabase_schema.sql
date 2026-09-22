-- Financial Help Hub - Supabase Database Schema
-- Run this SQL in your Supabase SQL Editor

-- 1. Create help_requests table
CREATE TABLE IF NOT EXISTS help_requests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    district TEXT NOT NULL,
    category TEXT NOT NULL CHECK (category IN ('Medical', 'Education', 'Emergency')),
    amount_needed INTEGER NOT NULL CHECK (amount_needed > 0),
    contact TEXT NOT NULL,
    short_description TEXT NOT NULL,
    detailed_message TEXT NOT NULL,
    photo_url TEXT,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'closed', 'fulfilled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 2. Create districts reference table
CREATE TABLE IF NOT EXISTS districts (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    state TEXT DEFAULT 'Tamil Nadu'
);

-- 3. Create categories reference table
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- 4. Insert Tamil Nadu districts
INSERT INTO districts (name, state) VALUES
    ('Chennai', 'Tamil Nadu'),
    ('Coimbatore', 'Tamil Nadu'),
    ('Madurai', 'Tamil Nadu'),
    ('Salem', 'Tamil Nadu'),
    ('Trichy', 'Tamil Nadu'),
    ('Tirunelveli', 'Tamil Nadu'),
    ('Erode', 'Tamil Nadu'),
    ('Vellore', 'Tamil Nadu'),
    ('Thanjavur', 'Tamil Nadu'),
    ('Kanyakumari', 'Tamil Nadu')
ON CONFLICT (name) DO NOTHING;

-- 5. Insert categories
INSERT INTO categories (name, description) VALUES
    ('Medical', 'Medical treatment and hospital expenses'),
    ('Education', 'School fees, college tuition, and educational expenses'),
    ('Emergency', 'Unexpected financial emergencies')
ON CONFLICT (name) DO NOTHING;

-- 6. Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_help_requests_status ON help_requests(status);
CREATE INDEX IF NOT EXISTS idx_help_requests_category ON help_requests(category);
CREATE INDEX IF NOT EXISTS idx_help_requests_district ON help_requests(district);
CREATE INDEX IF NOT EXISTS idx_help_requests_created_at ON help_requests(created_at DESC);

-- 7. Create updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_help_requests_updated_at
    BEFORE UPDATE ON help_requests
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- 8. Enable Row Level Security (RLS)
ALTER TABLE help_requests ENABLE ROW LEVEL SECURITY;
ALTER TABLE districts ENABLE ROW LEVEL SECURITY;
ALTER TABLE categories ENABLE ROW LEVEL SECURITY;

-- 9. Create policies for public read access
CREATE POLICY "Allow public read access" ON help_requests
    FOR SELECT USING (true);

CREATE POLICY "Allow public insert" ON help_requests
    FOR INSERT WITH CHECK (true);

CREATE POLICY "Allow public read on districts" ON districts
    FOR SELECT USING (true);

CREATE POLICY "Allow public read on categories" ON categories
    FOR SELECT USING (true);

-- 10. Insert sample demo data
INSERT INTO help_requests (name, district, category, amount_needed, contact, short_description, detailed_message, status) VALUES
    ('Meena', 'Chennai', 'Medical', 75000, 'meena.demo@example.com', 'My family is seeking financial assistance for my mother''s medical treatment.', 'My family is seeking financial assistance for my mother''s medical treatment. Any support or sharing of this request would mean a lot to our family.', 'active'),
    ('Arun', 'Madurai', 'Education', 40000, 'arun.demo@example.com', 'I am a college student and need assistance with my upcoming education expenses.', 'I am a college student and need assistance with my upcoming education expenses. I am seeking support to continue my studies.', 'active'),
    ('Kavitha', 'Coimbatore', 'Medical', 120000, 'kavitha.demo@example.com', 'Our family is seeking help with hospital expenses following an unexpected medical emergency.', 'Our family is seeking help with hospital expenses following an unexpected medical emergency.', 'active'),
    ('Suresh', 'Salem', 'Education', 30000, 'suresh.demo@example.com', 'I am seeking assistance with tuition and educational expenses.', 'I am seeking assistance with tuition and educational expenses so I can continue my studies.', 'active'),
    ('Priya', 'Tirunelveli', 'Emergency', 50000, 'priya.demo@example.com', 'Our family is facing an unexpected financial emergency.', 'Our family is facing an unexpected financial emergency and is seeking temporary assistance.', 'active'),
    ('David', 'Trichy', 'Medical', 90000, 'david.demo@example.com', 'We are seeking financial assistance for necessary medical treatment.', 'We are seeking financial assistance for necessary medical treatment. Any contribution or help sharing this request would be appreciated.', 'active');

-- Done! Your database schema is ready.