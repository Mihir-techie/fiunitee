# 🌟 Fiunite - Connect Through Vibes

A beautiful, modern social networking web application that connects people through shared vibes and activities. Built with Flask and featuring a stunning, mobile-responsive UI.

## ✨ Features

### 🎨 Modern Design
- **Beautiful UI/UX**: Stunning gradient backgrounds, glassmorphism effects, and smooth animations
- **Mobile Responsive**: Perfect experience across all devices - desktop, tablet, and mobile
- **Interactive Elements**: Hover effects, floating animations, and micro-interactions
- **Modern Typography**: Clean, readable fonts with proper hierarchy

### 🔐 User Authentication
- **Secure Registration**: Email-based account creation with validation
- **OTP Verification**: 6-digit email verification with beautiful UI
- **Login System**: Secure authentication with form validation
- **Session Management**: Proper user session handling

### 💫 Vibe Matching System
- **Vibe Selection**: Choose from multiple vibe types (Geeky, Chill, Energetic, Romantic, Adventurous, Creative)
- **Activity Matching**: Select from various activities (Robotics, Reading, Music, Sports, Gaming, Hiking, Cooking, Photography)
- **Time-based Matching**: Set availability dates and times
- **Smart Cards**: Beautiful user cards with connection features

### 🚀 User Experience
- **Splash Screen**: Animated welcome screen with floating elements
- **Hero Sections**: Engaging landing pages with call-to-actions
- **Loading States**: Smooth transitions and loading indicators
- **Error Handling**: User-friendly error messages and validation
- **Success Feedback**: Celebratory success pages with animations

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with proper schema management
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS framework with CSS Variables
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Poppins)
- **Animations**: CSS3 animations and transitions
- **Email**: Flask-Mail for OTP verification

## 🎯 Key Pages

### 1. **Splash Screen** (`/`)
- Animated logo with floating icons
- Smooth transition to welcome page
- Modern gradient background with particles

### 2. **Welcome Page** (`/welcome`)
- Hero section with compelling messaging
- Feature showcase with animated cards
- Statistics section
- Call-to-action buttons

### 3. **Authentication Pages**
- **Login** (`/login`): Clean form with validation
- **Signup** (`/signup`): Registration with password strength indicator
- **OTP Request** (`/otp`): Email verification request
- **OTP Verification** (`/verify_otp`): 6-digit code input with auto-focus
- **Success** (`/verify_success`): Celebration page with auto-redirect

### 4. **Core Features**
- **Vibe Form** (`/vibe_form`): Interactive vibe and activity selection
- **Vibe Matches** (`/vibe`): Beautiful user cards with connection options

## 🎨 Design System

### Color Palette
- **Primary**: #6366f1 (Indigo)
- **Secondary**: #ec4899 (Pink)
- **Accent**: #f59e0b (Amber)
- **Gradients**: Beautiful multi-color gradients
- **Neutrals**: Proper grayscale for text and backgrounds

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700, 800
- **Hierarchy**: Clear heading and body text sizes

### Components
- **Cards**: Glassmorphism effect with subtle shadows
- **Buttons**: Gradient backgrounds with hover animations
- **Forms**: Clean inputs with focus states
- **Navigation**: Responsive navbar with user state

### Animations
- **Page Transitions**: Smooth slide-in effects
- **Hover Effects**: Scale and shadow transformations
- **Floating Elements**: Subtle background animations
- **Loading States**: Spinner animations and progress bars

## 📱 Mobile Responsive Design

### Breakpoints
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: 320px - 767px

### Mobile Optimizations
- Touch-friendly button sizes
- Optimized form layouts
- Responsive grid systems
- Mobile navigation patterns

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fiunite
   ```

2. **Install dependencies**
   ```bash
   pip install flask flask-mail
   ```

3. **Configure email settings**
   - Edit `app.py` and update email configuration:
   ```python
   app.config['MAIL_USERNAME'] = "yourgmail@gmail.com"
   app.config['MAIL_PASSWORD'] = "your_app_password_here"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Enjoy the beautiful Fiunite experience!

## 🎯 User Journey

1. **Landing**: Users see the animated splash screen
2. **Welcome**: Compelling hero section with feature highlights
3. **Registration**: Clean signup form with validation
4. **Verification**: Beautiful OTP verification process
5. **Vibe Setting**: Interactive vibe and activity selection
6. **Matching**: Discover and connect with like-minded people

## 🔧 Customization

### Adding New Vibes
Edit `templates/vibe_form.html` and add new vibe options:
```html
<div class="vibe-option" data-value="NewVibe">
  <i class="fas fa-icon"></i>
  <span>New Vibe</span>
</div>
```

### Adding New Activities
Add new activity options in the same file:
```html
<div class="activity-option" data-value="NewActivity">
  <i class="fas fa-icon"></i>
  <span>New Activity</span>
</div>
```

### Customizing Colors
Update CSS variables in `static/style.css`:
```css
:root {
  --primary: #your-color;
  --secondary: #your-color;
  --accent: #your-color;
}
```

## 🎉 Features Highlights

### ✨ Beautiful Animations
- Floating background elements
- Smooth page transitions
- Interactive hover effects
- Loading animations
- Success celebrations

### 📱 Mobile-First Design
- Responsive layouts
- Touch-friendly interfaces
- Optimized for all screen sizes
- Fast loading on mobile devices

### 🎨 Modern UI Components
- Glassmorphism cards
- Gradient buttons
- Interactive forms
- Beautiful typography
- Consistent spacing

### 🔒 Security Features
- Email verification
- Session management
- Form validation
- Secure password handling

## 🌟 Why Fiunite?

Fiunite represents the future of social networking - connecting people through shared vibes and activities rather than superficial profiles. The beautiful, modern interface makes the experience delightful while the smart matching system ensures meaningful connections.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support, email support@fiunite.com or create an issue in the repository.

---

**Made with ❤️ for connecting people through vibes**
