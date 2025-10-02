# 🚂 Railway Deployment Guide

## Quick Deploy (3 Minutes)

### Step 1: Prepare Your Repository
```bash
git add .
git commit -m "Railway deployment ready"
git push origin main
```

### Step 2: Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository
5. Railway will auto-detect Python/FastAPI

### Step 3: Add PostgreSQL Database

1. In your Railway project, click **"+ New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Railway automatically sets `DATABASE_URL` environment variable

### Step 4: Configure Environment Variables

Go to your service → **Variables** tab and add:

```bash
# Required Variables
SENDGRID_API_KEY=SG.your_sendgrid_api_key
JWT_SECRET=your_secure_random_string_here

# Optional Variables
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
PERPLEXITY_API_KEY=pplx-your_api_key

# CORS Configuration (Update after deployment)
ALLOWED_ORIGINS=https://your-app.railway.app
BASE_URL=https://your-app.railway.app
```

### Step 5: Update CORS After First Deploy

1. After first deployment, Railway gives you a URL like: `https://your-app.railway.app`
2. Update these environment variables:
   ```bash
   ALLOWED_ORIGINS=https://your-app.railway.app
   BASE_URL=https://your-app.railway.app
   ```
3. Redeploy (Railway auto-redeploys on variable changes)

## ✅ Verification Checklist

After deployment, verify:

- [ ] App is running: `https://your-app.railway.app`
- [ ] API docs accessible: `https://your-app.railway.app/docs`
- [ ] Database connected (check logs)
- [ ] SendGrid configured (test email sending)
- [ ] No CORS errors in browser console

## 🔧 Troubleshooting

### Issue: "Network Error" or Connection Refused

**Solution:**
```bash
# Check these environment variables are set:
PORT=8000  # Railway sets this automatically
HOST=0.0.0.0
DATABASE_URL=postgresql://...?sslmode=require
```

### Issue: CORS Errors

**Solution:**
```bash
# Update ALLOWED_ORIGINS with your Railway domain:
ALLOWED_ORIGINS=https://your-app.railway.app,https://your-custom-domain.com
```

### Issue: Database Connection Failed

**Solution:**
```bash
# Ensure DATABASE_URL has SSL mode:
DATABASE_URL=postgresql://user:pass@host:5432/db?sslmode=require

# Or use Neon database (already has SSL):
DATABASE_URL=postgresql://user:pass@ep-xxx.neon.tech/db?sslmode=require
```

### Issue: SendGrid 403 Forbidden

**Solution:**
1. Verify SendGrid API key has "Mail Send" permissions
2. Verify sender email is verified in SendGrid dashboard
3. Check API key is correctly set in Railway environment variables

### Issue: App Crashes on Startup

**Check Railway Logs:**
```bash
# In Railway dashboard → Deployments → View Logs
```

Common fixes:
- Missing required environment variables (JWT_SECRET, SENDGRID_API_KEY)
- Database connection issues
- Port binding issues (ensure using $PORT)

## 📊 Monitoring

### View Logs
Railway Dashboard → Your Service → Deployments → View Logs

### Check Health
```bash
curl https://your-app.railway.app/docs
```

### Database Connection
```bash
# Railway provides database connection info in Variables tab
```

## 🚀 Performance Tips

1. **Use Connection Pooling** (Already configured in database.py)
2. **Enable Gunicorn Workers** (Already configured in Procfile)
3. **Set Proper Timeouts** (Already configured - 120s)
4. **Monitor Memory Usage** (Railway dashboard)

## 💰 Cost Estimate

- **Railway Free Tier**: $5 free credit/month
- **Hobby Plan**: $5/month (includes PostgreSQL)
- **Pro Plan**: $20/month (better performance)

## 🔒 Security Checklist

- [ ] JWT_SECRET is a strong random string (32+ characters)
- [ ] DATABASE_URL uses SSL (sslmode=require)
- [ ] SENDGRID_API_KEY is kept secret
- [ ] ALLOWED_ORIGINS is set to your domain only
- [ ] Google OAuth credentials are secure

## 📝 Post-Deployment

1. **Test all features:**
   - User registration/login
   - Email sending
   - Template management
   - Admin panel

2. **Set up custom domain** (Optional):
   - Railway Settings → Domains → Add Custom Domain

3. **Enable monitoring:**
   - Railway provides built-in metrics
   - Set up alerts for downtime

## 🆘 Need Help?

1. Check Railway logs first
2. Verify all environment variables
3. Test database connection
4. Validate SendGrid configuration
5. Check CORS settings

## 🎯 Quick Commands

```bash
# View logs
railway logs

# Restart service
railway restart

# Open in browser
railway open

# Check status
railway status
```

---

**Your app should now be running smoothly on Railway! 🎉**

Access your app at: `https://your-app.railway.app`
