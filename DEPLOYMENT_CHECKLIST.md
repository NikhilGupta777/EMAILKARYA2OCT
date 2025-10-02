# ✅ Railway Deployment Checklist

## Pre-Deployment (Local Testing)

- [ ] Test locally: `python main.py`
- [ ] Verify database connection works
- [ ] Test email sending with SendGrid
- [ ] Check all environment variables in `.env`
- [ ] Commit all changes to Git
- [ ] Push to GitHub

## Railway Setup

- [ ] Create Railway account at [railway.app](https://railway.app)
- [ ] Connect GitHub account
- [ ] Create new project from GitHub repo
- [ ] Add PostgreSQL database to project
- [ ] Note your Railway app URL (e.g., `https://your-app.railway.app`)

## Environment Variables Configuration

Copy these to Railway → Variables tab:

### Required Variables ✅
- [ ] `SENDGRID_API_KEY` - Your SendGrid API key
- [ ] `JWT_SECRET` - Random secure string (32+ characters)
- [ ] `DATABASE_URL` - Auto-set by Railway PostgreSQL
- [ ] `ALLOWED_ORIGINS` - Your Railway app URL
- [ ] `BASE_URL` - Your Railway app URL

### Optional Variables
- [ ] `GOOGLE_CLIENT_ID` - For Google OAuth
- [ ] `GOOGLE_CLIENT_SECRET` - For Google OAuth
- [ ] `PERPLEXITY_API_KEY` - For AI email generation

### Auto-Set by Railway
- [ ] `PORT` - Railway sets this automatically
- [ ] `HOST` - Should be `0.0.0.0`

## Post-Deployment Verification

### 1. Check Deployment Status
- [ ] Railway shows "Deployed" status
- [ ] No errors in deployment logs
- [ ] Build completed successfully

### 2. Test API Endpoints
- [ ] Health check: `https://your-app.railway.app/health`
- [ ] API docs: `https://your-app.railway.app/docs`
- [ ] Frontend: `https://your-app.railway.app/`

### 3. Test Core Features
- [ ] User registration works
- [ ] User login works
- [ ] Email sending works
- [ ] Template management works
- [ ] Admin panel accessible

### 4. Check Logs
- [ ] No database connection errors
- [ ] No CORS errors
- [ ] No SendGrid authentication errors
- [ ] Application starts successfully

## Common Issues & Quick Fixes

### ❌ Network Error / Connection Refused
**Fix:**
```bash
# Ensure these are set in Railway:
PORT=8000  # Auto-set by Railway
HOST=0.0.0.0
```

### ❌ CORS Error in Browser
**Fix:**
```bash
# Update in Railway Variables:
ALLOWED_ORIGINS=https://your-app.railway.app
BASE_URL=https://your-app.railway.app
```

### ❌ Database Connection Failed
**Fix:**
```bash
# Ensure DATABASE_URL has SSL:
DATABASE_URL=postgresql://...?sslmode=require
```

### ❌ SendGrid 403 Error
**Fix:**
1. Verify API key has "Mail Send" permissions
2. Verify sender email is verified in SendGrid
3. Check API key is correct in Railway

### ❌ App Crashes on Startup
**Check:**
1. Railway logs for error messages
2. All required env variables are set
3. Database is running
4. No syntax errors in code

## Performance Optimization

- [ ] Connection pooling enabled (✅ Already configured)
- [ ] Gunicorn workers configured (✅ Already configured)
- [ ] Timeout settings appropriate (✅ 120s)
- [ ] SSL/TLS enabled for database (✅ Already configured)

## Security Checklist

- [ ] JWT_SECRET is strong and random
- [ ] Database uses SSL connection
- [ ] SENDGRID_API_KEY is kept secret
- [ ] ALLOWED_ORIGINS restricted to your domain
- [ ] No sensitive data in logs
- [ ] Environment variables not in Git

## Monitoring Setup

- [ ] Check Railway metrics dashboard
- [ ] Set up alerts for downtime (Railway Pro)
- [ ] Monitor database usage
- [ ] Monitor memory/CPU usage
- [ ] Check error logs regularly

## Optional: Custom Domain

- [ ] Purchase domain (if needed)
- [ ] Add custom domain in Railway settings
- [ ] Update DNS records
- [ ] Update `ALLOWED_ORIGINS` and `BASE_URL`
- [ ] Test with custom domain

## Final Verification

- [ ] All features work as expected
- [ ] No errors in browser console
- [ ] No errors in Railway logs
- [ ] Email sending works
- [ ] Database queries work
- [ ] Authentication works
- [ ] Admin panel works

## 🎉 Deployment Complete!

Your app is now live at: `https://your-app.railway.app`

### Next Steps:
1. Share the URL with users
2. Monitor logs for any issues
3. Set up regular backups
4. Consider upgrading to Railway Pro for better performance

### Support:
- Railway Docs: https://docs.railway.app
- Project Issues: Check GitHub issues
- Railway Discord: https://discord.gg/railway

---

**Congratulations! Your email management system is now deployed! 🚀**
