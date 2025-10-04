# 🚀 Fiunite Deployment Guide

## 📋 Prerequisites
- GitHub account with repository: https://github.com/Mihir-techie/fiunitee.git
- Render account (free tier available)
- Gmail account for email functionality

## 🔧 Setup Steps

### 1. Push Code to GitHub
```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - Fiunite Flask app ready for deployment"

# Add remote repository
git remote add origin https://github.com/Mihir-techie/fiunitee.git

# Push to GitHub
git push -u origin main
```

### 2. Gmail App Password Setup
1. Go to your Google Account settings
2. Enable 2-Factor Authentication
3. Generate an App Password for "Mail"
4. Use this password in Render environment variables

### 3. Deploy on Render

#### Step 1: Create New Web Service
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository: `Mihir-techie/fiunitee`
4. Select the repository

#### Step 2: Configure Build Settings
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Environment**: `Python 3`

#### Step 3: Set Environment Variables
Add these environment variables in Render dashboard:

```
SECRET_KEY = your-very-secure-secret-key-here
MAIL_USERNAME = yourgmail@gmail.com
MAIL_PASSWORD = your-gmail-app-password
```

#### Step 4: Deploy
- Click "Create Web Service"
- Wait for deployment to complete (5-10 minutes)
- Your app will be available at: `https://your-app-name.onrender.com`

## 🔐 Security Notes
- Never commit sensitive data to GitHub
- Use environment variables for all secrets
- Keep your Gmail app password secure
- The app uses SQLite which will reset on each deployment

## 📱 Features Included
- ✅ Beautiful responsive UI
- ✅ User authentication (signup/login)
- ✅ Email verification with OTP
- ✅ Profile creation with about form
- ✅ Vibe matching system
- ✅ Mobile-optimized design
- ✅ Modern animations and effects

## 🛠️ Troubleshooting
- If deployment fails, check build logs in Render dashboard
- Ensure all environment variables are set correctly
- Gmail may require app password instead of regular password
- Database resets on each deployment (normal for free tier)

## 🌟 Your App is Ready!
Once deployed, your Fiunite app will be live and accessible worldwide with a beautiful, modern interface!
