@echo off
echo ========================================
echo Pushing Railway Deployment Fixes to GitHub
echo ========================================
echo.

REM Check if git is initialized
if not exist .git (
    echo Initializing git repository...
    git init
    git remote add origin https://github.com/NikhilGupta777/EMAILKARYA2OCT.git
)

echo.
echo Adding all files...
git add .

echo.
echo Committing changes...
git commit -m "Railway deployment fixes - All network errors resolved"

echo.
echo Pushing to GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo SUCCESS! All changes pushed to GitHub
    echo ========================================
    echo.
    echo Repository: https://github.com/NikhilGupta777/EMAILKARYA2OCT
    echo.
    echo Next Steps:
    echo 1. Go to railway.app
    echo 2. Deploy from GitHub repo
    echo 3. Follow QUICK_DEPLOY.md
    echo.
) else (
    echo.
    echo ========================================
    echo ERROR: Failed to push to GitHub
    echo ========================================
    echo.
    echo Possible solutions:
    echo 1. Check your internet connection
    echo 2. Verify GitHub credentials
    echo 3. Try: git push -f origin main
    echo.
)

pause
