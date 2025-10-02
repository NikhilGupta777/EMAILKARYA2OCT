# ⚡ Quick Deploy to Railway (2 Minutes)

## Step 1: Push to GitHub (30 seconds)
```bash
git add .
git commit -m "Ready for Railway deployment"
git push origin main
```

## Step 2: Deploy to Railway (1 minute)
1. Go to **[railway.app](https://railway.app)**
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select your repository
4. Railway auto-detects and starts building

## Step 3: Add Database (30 seconds)
1. In your project, click **"+ New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Done! `DATABASE_URL` is auto-set

## Step 4: Set Environment Variables (30 seconds)
Go to your service → **Variables** tab:

```bash
SENDGRID_API_KEY=SG.your_sendgrid_api_key
JWT_SECRET=your_secure_random_string_32_chars
```

## Step 5: Update CORS (After First Deploy)
After Railway gives you a URL (e.g., `https://your-app.railway.app`):

```bash
ALLOWED_ORIGINS=https://your-app.railway.app
BASE_URL=https://your-app.railway.app
```

Railway will auto-redeploy.

---

## ✅ Verify Deployment

1. **Health Check:** `https://your-app.railway.app/health`
2. **API Docs:** `https://your-app.railway.app/docs`
3. **Frontend:** `https://your-app.railway.app/`

---

## 🎉 Done!

Your app is now live and working smoothly!

**Need help?** See [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md)

**Troubleshooting?** See [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)

**Check config?** Run `python debug_railway.py`
