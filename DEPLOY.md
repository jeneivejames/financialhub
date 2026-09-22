# Financial Help Hub - Deployment Guide

This app is **100% platform-agnostic** with NO Databricks dependencies. Deploy it anywhere!

## ✅ What You Need

1. **Supabase Database** (already set up)
   - URL: `https://tzrcjamabhduxezmeyze.supabase.co`
   - Anon Key: (your SUPABASE_KEY)

2. **Files to Deploy**:
   - `app.py` - Flask backend
   - `database.py` - Supabase connection
   - `index.html`, `style.css`, `script.js` - Frontend
   - `requirements.txt` - Python dependencies
   - `Procfile` - Web server command
   - `runtime.txt` - Python version

---

## 🚀 Quick Deploy Options

### Option 1: Heroku (Easiest - Free Tier Available)

```bash
# 1. Install Heroku CLI
# Download from: https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Create app
heroku create your-app-name

# 4. Set environment variables
heroku config:set SUPABASE_URL=https://tzrcjamabhduxezmeyze.supabase.co
heroku config:set SUPABASE_KEY=your_supabase_anon_key

# 5. Deploy
git init
git add .
git commit -m "Initial commit"
git push heroku main

# 6. Open your app
heroku open
```

**Your app will be at:** `https://your-app-name.herokuapp.com`

---

### Option 2: Render.com (Free Tier, Zero Config)

1. **Sign up** at https://render.com
2. **New Web Service** → Connect your GitHub repo or upload files
3. **Settings**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. **Environment Variables**:
   - `SUPABASE_URL` = `https://tzrcjamabhduxezmeyze.supabase.co`
   - `SUPABASE_KEY` = `your_supabase_anon_key`
5. **Deploy**

**Your app will be at:** `https://your-app-name.onrender.com`

---

### Option 3: Railway.app (Modern, Fast)

1. **Sign up** at https://railway.app
2. **New Project** → **Deploy from GitHub** or upload files
3. **Add Environment Variables**:
   - `SUPABASE_URL` = `https://tzrcjamabhduxezmeyze.supabase.co`
   - `SUPABASE_KEY` = `your_supabase_anon_key`
4. **Deploy** (auto-detects Python and uses Procfile)

**Your app will be at:** `https://your-app-name.railway.app`

---

### Option 4: Vercel (Serverless)

1. Install Vercel CLI: `npm install -g vercel`
2. Create `vercel.json`:
```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "SUPABASE_URL": "https://tzrcjamabhduxezmeyze.supabase.co",
    "SUPABASE_KEY": "your_supabase_anon_key"
  }
}
```
3. Run: `vercel --prod`

---

### Option 5: AWS EC2 (Full Control)

```bash
# 1. SSH into your EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# 2. Install Python and dependencies
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

# 3. Set environment variables
export SUPABASE_URL=https://tzrcjamabhduxezmeyze.supabase.co
export SUPABASE_KEY=your_supabase_anon_key

# 4. Run with gunicorn
gunicorn app:app --bind 0.0.0.0:80
```

---

### Option 6: DigitalOcean App Platform

1. **Sign up** at https://digitalocean.com
2. **Create App** → Connect GitHub or upload
3. **Detected Buildpack**: Python
4. **Environment Variables**:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
5. **Deploy**

---

## 🔧 Local Development

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables
export SUPABASE_URL=https://tzrcjamabhduxezmeyze.supabase.co
export SUPABASE_KEY=your_supabase_anon_key

# 3. Run locally
python app.py

# App runs at: http://localhost:5000
```

---

## 📦 Files Structure

```
financial-help-hub/
├── app.py              # Flask backend (NO Databricks code)
├── database.py         # Supabase connection
├── index.html          # Homepage
├── style.css           # Styles
├── script.js           # Frontend logic
├── requirements.txt    # Python dependencies
├── Procfile           # Web server command (Heroku/Railway)
├── runtime.txt        # Python version
├── supabase_schema.sql # Database setup (run once in Supabase)
└── DEPLOY.md          # This file
```

---

## 🔐 Environment Variables Required

| Variable       | Value                                            |
|----------------|--------------------------------------------------|
| SUPABASE_URL   | `https://tzrcjamabhduxezmeyze.supabase.co`      |
| SUPABASE_KEY   | Your Supabase anon key (from Supabase dashboard)|

---

## ✅ Verification

After deployment, test these endpoints:

1. **Homepage**: `https://your-app.com/`
2. **API Health**: `https://your-app.com/health`
3. **Get Requests**: `https://your-app.com/api/requests`

---

## 🎯 No Databricks Required!

This app is **completely independent** of Databricks:
- ✅ Pure Flask + Supabase
- ✅ No Databricks SDK
- ✅ No Databricks authentication
- ✅ Works on ANY Python hosting platform
- ✅ 100% open-source stack

---

## 🐛 Troubleshooting

**Error: Database connection failed**
- Check environment variables are set correctly
- Verify SUPABASE_KEY is the anon key (not service role)
- Run `fix_rls_policies.sql` in Supabase if getting 401 errors

**Error: Port already in use**
- Platform will set PORT automatically
- Locally: Use different port with `PORT=8080 python app.py`

**Error: Module not found**
- Run: `pip install -r requirements.txt`

---

## 📚 Platform-Specific Docs

- **Heroku**: https://devcenter.heroku.com/articles/getting-started-with-python
- **Render**: https://render.com/docs/deploy-flask
- **Railway**: https://docs.railway.app/develop/services
- **Vercel**: https://vercel.com/docs/functions/serverless-functions/runtimes/python
- **DigitalOcean**: https://docs.digitalocean.com/products/app-platform/

---

**Need help?** Open an issue or contact support for your chosen platform.
