# Django Blog Authentication System

## Overview
This authentication system enables user registration, login, logout, and profile management using Django’s built-in views and custom forms.

## Views and Forms
- `register`: Custom view using `CustomUserCreationForm` to create new users with email
- `login`: Django’s built-in `LoginView`
- `logout`: Django’s built-in `LogoutView`
- `profile`: Custom view to view and update user email

## Templates
- `register.html`: Form for new users
- `login.html`: Login form with error feedback
- `logout.html`: Confirmation page
- `profile.html`: Displays and updates user email

All templates include `{% csrf_token %}` for security.

## URL Paths
- `/register`: Registration page
- `/login`: Login page
- `/logout`: Logout page
- `/profile`: Profile management

## Testing Instructions
1. Register a new user at `/register`
2. Log in at `/login`
3. Visit `/profile` to view and update email
4. Log out via `/logout`

Edge cases:
- Invalid credentials
- Duplicate usernames
- Blank profile fields

## Security Notes
- CSRF protection enabled via `{% csrf_token %}`
- Passwords hashed using Django’s default PBKDF2