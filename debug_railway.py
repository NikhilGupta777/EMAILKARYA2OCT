#!/usr/bin/env python3
"""
Railway Deployment Debug Script
Run this to check if your environment is properly configured for Railway
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def check_env_var(name, required=True):
    """Check if environment variable is set"""
    value = os.getenv(name)
    if value:
        # Mask sensitive values
        if 'KEY' in name or 'SECRET' in name or 'PASSWORD' in name:
            masked = value[:4] + '*' * (len(value) - 8) + value[-4:] if len(value) > 8 else '***'
            print(f"✅ {name}: {masked}")
        else:
            print(f"✅ {name}: {value}")
        return True
    else:
        if required:
            print(f"❌ {name}: NOT SET (REQUIRED)")
        else:
            print(f"⚠️  {name}: NOT SET (OPTIONAL)")
        return not required

def check_database_url():
    """Check database URL format"""
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("❌ DATABASE_URL not set")
        return False
    
    if "postgresql" not in db_url:
        print("⚠️  DATABASE_URL doesn't appear to be PostgreSQL")
        return False
    
    if "sslmode" not in db_url:
        print("⚠️  DATABASE_URL missing sslmode parameter (should have ?sslmode=require)")
        return False
    
    print("✅ DATABASE_URL format looks good")
    return True

def check_cors_config():
    """Check CORS configuration"""
    origins = os.getenv("ALLOWED_ORIGINS", "")
    base_url = os.getenv("BASE_URL", "")
    
    if not origins:
        print("⚠️  ALLOWED_ORIGINS not set - will allow all origins (*)")
        return False
    
    if "localhost" in origins and "railway.app" not in origins:
        print("⚠️  ALLOWED_ORIGINS contains localhost but no Railway domain")
        print("   Update to include your Railway app URL")
        return False
    
    if not base_url:
        print("⚠️  BASE_URL not set")
        return False
    
    print("✅ CORS configuration looks good")
    return True

def check_port_config():
    """Check port configuration"""
    port = os.getenv("PORT")
    host = os.getenv("HOST")
    
    if not port:
        print("⚠️  PORT not set (Railway will set this automatically)")
    else:
        print(f"✅ PORT: {port}")
    
    if not host or host != "0.0.0.0":
        print("⚠️  HOST should be 0.0.0.0 for Railway")
    else:
        print(f"✅ HOST: {host}")
    
    return True

def main():
    print("=" * 60)
    print("🚂 RAILWAY DEPLOYMENT CONFIGURATION CHECK")
    print("=" * 60)
    print()
    
    print("📋 Required Environment Variables:")
    print("-" * 60)
    all_good = True
    all_good &= check_env_var("DATABASE_URL", required=True)
    all_good &= check_env_var("SENDGRID_API_KEY", required=True)
    all_good &= check_env_var("JWT_SECRET", required=True)
    print()
    
    print("📋 Optional Environment Variables:")
    print("-" * 60)
    check_env_var("GOOGLE_CLIENT_ID", required=False)
    check_env_var("GOOGLE_CLIENT_SECRET", required=False)
    check_env_var("PERPLEXITY_API_KEY", required=False)
    print()
    
    print("📋 Railway Configuration:")
    print("-" * 60)
    check_env_var("ALLOWED_ORIGINS", required=False)
    check_env_var("BASE_URL", required=False)
    check_port_config()
    print()
    
    print("📋 Detailed Checks:")
    print("-" * 60)
    check_database_url()
    check_cors_config()
    print()
    
    print("=" * 60)
    if all_good:
        print("✅ All required variables are set!")
        print("🚀 Your app should deploy successfully to Railway")
    else:
        print("❌ Some required variables are missing")
        print("⚠️  Please set them in Railway's Variables tab")
    print("=" * 60)
    print()
    
    print("📝 Next Steps:")
    print("1. Fix any issues shown above")
    print("2. Set missing variables in Railway dashboard")
    print("3. Redeploy your app")
    print("4. Check Railway logs for any errors")
    print()
    
    print("📚 Documentation:")
    print("- Railway Guide: RAILWAY_DEPLOYMENT.md")
    print("- Deployment Checklist: DEPLOYMENT_CHECKLIST.md")
    print()

if __name__ == "__main__":
    main()
