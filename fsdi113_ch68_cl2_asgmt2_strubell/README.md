# Assignment 2 — Protecting Views and Templates
## FSDI 113 — Intermediate Django
## Strubell Goods & Gear (SGnG) Blog Security System

---

# Overview
This project implements the requirements for Assignment 2 of FSDI‑113. The goal is to secure a Django blog application using LoginRequiredMixin and UserPassesTestMixin, protect templates, and implement custom error pages. The project also includes SGnG‑styled templates and a light/dark mode UI.

The application contains two main apps:
- accounts — handles login and logout
- blog — handles posts, draft views, archived views, and protected content
The project is fully isolated from Assignment 1 and built from scratch.

---

# Features Implemented

## Authentication
- Login page
- Logout page
- Profile page (optional, used for future assignments)

## Authorization
- LoginRequiredMixin applied to draft and archived views
- UserPassesTestMixin applied to protected post detail view
- Custom 403, 404, and 500 error templates

## Blog Functionality
- Published posts list
- Draft posts list (visible only to the logged‑in author)
- Archived posts list (visible only to the logged‑in author)
- Protected post detail view
- SGnG‑styled templates for all blog pages

## SGnG UI Enhancements
- SGnG brand styling
- Bevel and emboss effects
- Glow accents
- Light/dark mode toggle
- Global base template
- SGnG navigation bar with conditional rendering based on authentication state

---

# Project Structure
fsdi113_ch68_cl2_asgmt2_strubell/
│
├── manage.py
├── sgng_blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── views.py
│   ├── urls.py
│   └── templates/accounts/
│       ├── login.html
│       └── logout.html
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/blog/
│       ├── post_list.html
│       ├── post_detail.html
│       ├── post_draft_list.html
│       └── post_archived_list.html
│
├── templates/
│   ├── base.html
│   ├── 403.html
│   ├── 404.html
│   └── 500.html
│
└── static/css/styles.css

---

# How to Run the Project (via PowerShell Terminal): 
1. Activate the virtual environment
  Code: .\venv113_cl2\Scripts\Activate.ps1
2. Install dependencies
  Code: pip install django
3. Apply migrations
  Code: python manage.py migrate
4. Create a superuser
  Code: python manage.py createsuperuser
5. Run the development server
  Code: python manage.py runserver
6. Access the application
  Open your browser and go to: http://127.0.0.1:8000/

---

# Authentication Flow
- Users log in through /accounts/login/.
- Logged‑in users gain access to:
  - Draft posts
  - Archived posts
  - Protected post detail views
- Unauthorized access triggers the custom 403 page.
- Missing pages trigger the custom 404 page.
- Server errors trigger the custom 500 page.

---

# Evidence of Functionality (for Assignment Report)

## Protected Views
- Draft and archived posts require authentication.
- Protected post detail view requires ownership.

## Mixins
- LoginRequiredMixin ensures only authenticated users can view drafts and archived posts.
- UserPassesTestMixin ensures only the author can view protected post details.

## Custom Error Templates
- 403, 404, and 500 templates are implemented and styled with SGnG branding.

---

# SGnG Branding
The project includes a custom SGnG UI theme:
- SGnG color palette
- Bevel and emboss effects
- Glow accents
- Light/dark mode toggle
- SGnG navigation bar
- SGnG typography and layout
All templates inherit from base.html.

---

# GitHub Repository
Insert your GitHub repository URL here.

---

# AI Disclosure
I used AI for help drafting written content. All code was written manually.
