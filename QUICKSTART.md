# 🚀 Financial Help Hub - Quick Start Guide

## 📦 Step 1: Get the Files

Download these **11 files** from your workspace:

```
/Users/jeneive.dhanapalan@gmail.com/financial-help-hub/

✓ app.py                # Main Flask application
✓ database.py           # Supabase connection
✓ index.html            # Frontend HTML
✓ style.css             # Styles
✓ script.js             # Frontend JavaScript
✓ requirements.txt      # Python dependencies
✓ Procfile             # Web server config
✓ runtime.txt          # Python version
✓ README.md            # Project overview
✓ DEPLOY.md            # Deployment guide
✓ .gitignore           # Git ignore rules
```

**DO NOT include:**
- ❌ `app.yaml` (Databricks-specific, not needed)
- ❌ `.env` (local development only)

---

## ☁️ Step 2: Choose Your Platform

### Option A: Heroku (Easiest - 5 minutes)

1. **Install Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli
2. **Commands**:
```bash
cd financial-help-hub
heroku login
heroku create your-app-name
heroku config:set SUPABASE_URL=https://tzrcjamabhduxezmeyze.supabase.co
heroku config:set SUPABASE_KEY=your_supabase_anon_key
git init
git add .
git commit -m "Initial commit"
git push heroku main
heroku open
```

**Done!** Your app is live at `https://your-app-name.herokuapp.com`

---

### Option B: Render.com (No CLI needed)

1. Go to https://render.com
2. Click **"New Web Service"**
3. Connect GitHub or upload files
4. **Settings**:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
5. **Environment**:
   - `SUPABASE_URL` = `https://tzrcjamabhduxezmeyze.supabase.co`
   - `SUPABASE_KEY` = `your_anon_key`
6. Click **Deploy**

**Done!** Your app is live at `https://your-app-name.onrender.com`

---

### Option C: Railway.app (Modern & Fast)

1. Go to https://railway.app
2. **New Project** → **Deploy from GitHub**
3. **Add Variables**:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
4. Click **Deploy**

**Done!** Your app is live at `https://your-app-name.railway.app`

---

## 🔐 Step 3: Get Your Supabase Keys

1. Go to https://supabase.com/dashboard
2. Select your project: `tzrcjamabhduxezmeyze`
3. Go to **Settings** → **API**
4. Copy:
   - **URL**: `https://tzrcjamabhduxezmeyze.supabase.co`
   - **anon public key**: `eyJhbGciOi...` (long string)

---

## 🧪 Step 4: Test Your App

After deployment, visit:

1. **Homepage**: `https://your-app.com/`
   - Should show "Financial Help Hub" title
   - Should display 6 demo requests

2. **Health Check**: `https://your-app.com/health`
   - Should show: `{"status": "healthy", "database": "connected"}`

3. **API Test**: `https://your-app.com/api/requests`
   - Should return JSON with help requests

---

## 🐛 Troubleshooting

**Problem: "Error loading requests"**
- Check environment variables are set correctly
- Verify Supabase URL and key
- Run `fix_rls_policies.sql` in Supabase SQL Editor

**Problem: App crashes on startup**
- Check logs: `heroku logs --tail` (Heroku)
- Verify all files uploaded correctly
- Check Python version matches `runtime.txt`

**Problem: "Database connection failed"**
- Verify SUPABASE_URL is set
- Verify SUPABASE_KEY is the **anon** key (not service_role)
- Check Supabase project is active

---

## 📚 Full Documentation

- **README.md** - Complete overview and features
- **DEPLOY.md** - Detailed deployment for 8 platforms
- **SETUP.md** - Supabase database setup

---

## ✨ That's It!

Your Financial Help Hub is now:
- ✅ Running on a public URL
- ✅ Accessible by anyone (no login required)
- ✅ Storing data in Supabase
- ✅ 100% independent of Databricks

**Share your app URL with the world!** 🌍

---

## 🆘 Need Help?

1. Check [DEPLOY.md](DEPLOY.md) for platform-specific guides
2. Check platform logs for error messages
3. Verify environment variables are set
4. Test Supabase connection directly

**Made with ❤️ for community support**
