# 🤝 Financial Help Hub

A community-driven platform where people can share genuine financial needs and connect with others who may be able to help.

## ✨ Features

- 📝 **Submit Help Requests** - Share your financial need with the community
- 🔍 **Browse Requests** - View help requests by category or district
- 💾 **Persistent Storage** - All data stored in Supabase cloud database
- 📱 **Mobile Responsive** - Works on all devices
- 🌐 **100% Open Source** - No proprietary dependencies

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Database**: Supabase (PostgreSQL)
- **Deployment**: Platform-agnostic (Heroku, Render, Railway, Vercel, AWS, etc.)

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Supabase account (free tier available)

### Local Development

```bash
# 1. Clone or download this repository

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment variables
export SUPABASE_URL=your_supabase_url
export SUPABASE_KEY=your_supabase_anon_key

# 4. Run the app
python app.py

# 5. Open browser
# http://localhost:5000
```

## 📦 Deployment

This app has **ZERO Databricks dependencies** and can be deployed anywhere!

See [DEPLOY.md](DEPLOY.md) for detailed deployment instructions for:
- ☁️ Heroku
- 🎨 Render.com
- 🚂 Railway.app
- ⚡ Vercel
- 🌊 DigitalOcean
- 📦 AWS EC2
- ...and any other Python hosting platform!

## 🗄️ Database Setup

1. Create a Supabase project at https://supabase.com
2. Run the SQL in `supabase_schema.sql` in the Supabase SQL Editor
3. Get your project URL and anon key from Settings → API
4. Set as environment variables (see above)

## 📁 Project Structure

```
financial-help-hub/
├── app.py              # Flask backend
├── database.py         # Supabase connection
├── index.html          # Homepage
├── style.css           # Styles
├── script.js           # Frontend logic
├── requirements.txt    # Dependencies
├── Procfile           # Production server
├── runtime.txt        # Python version
└── DEPLOY.md          # Deployment guide
```

## 🔐 Environment Variables

| Variable       | Description                     | Required |
|----------------|---------------------------------|----------|
| SUPABASE_URL   | Your Supabase project URL       | Yes      |
| SUPABASE_KEY   | Your Supabase anon key          | Yes      |
| PORT           | Server port (default: 5000)     | No       |

## 🧪 API Endpoints

- `GET /` - Homepage
- `GET /api/requests` - Get all help requests
- `GET /api/requests/<id>` - Get single request
- `POST /api/requests` - Create new request
- `GET /api/districts` - Get all districts
- `GET /api/categories` - Get all categories
- `GET /health` - Health check

## 🔒 Security

- ✅ Row Level Security (RLS) enabled on all tables
- ✅ Public read/insert only (no delete/update)
- ✅ Demo data clearly marked
- ⚠️ **Important**: Users should independently verify any request before sending money

## 📄 License

Open source - feel free to use, modify, and distribute.

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## ⚠️ Disclaimer

This is a demonstration platform. All sample requests are fictional. Users should independently verify any financial assistance requests before sending money.

## 📞 Support

For deployment help, see [DEPLOY.md](DEPLOY.md) or consult your hosting platform's documentation.

---

**Made with ❤️ for community support**
