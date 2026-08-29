### ASSIGNMENT 1 — Accounts Application
## Project Title: SGnG Authentication System
# FSDI-113 — Intermediate Django 

## PROJECT OVERVIEW
  This project implements the required “accounts” application for FSDI‑113 Assignment 1. The application provides user authentication functionality, allowing users to log in and log out using Django’s built‑in authentication system. The project also includes SGnG‑styled templates for a consistent user interface.

## FEATURES IMPLEMENTED
- Login functionality
- Logout functionality
- Home page confirming successful authentication
- Form validation for required fields
- Backend views for login, logout, signup, and profile
- Clean URL routing for authentication pages
- SGnG‑styled frontend templates

## PROJECT STRUCTURE
- accounts/          # Authentication views and templates
- sgng_blog/         # Main application views and error handlers
- templates/         # SGnG-styled HTML templates
- static/            # SGnG CSS styling
- manage.py          # Django project runner

## HOW TO RUN THE PROJECT 
1. Install Dependencies 
   - pip install -r requirements.txt 
2. Run Migrations
   - py manage.py migrate
3. Start the Development Server
   - py manage.py runserver
4. Visit the Application
   - http://127.0.0.1:8000/

## AUTHENTICATION FLOW
- Users can log in using the login page.
- After logging in, users are redirected to the SGnG home page.
- Users can log out using the logout link.
- Validation errors appear if required fields are left empty.


