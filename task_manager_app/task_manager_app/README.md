# Task Manager App Django Project Documentation

The `task_manager_app` directory contains the core Django project configuration that ties together all applications and provides the foundational settings for the Mini Task Manager application. This serves as the central configuration hub for the entire backend system.

## Project Overview

This Django project follows standard Django conventions while implementing modern best practices for API development, security, and cross-origin resource sharing. It's configured specifically to work as a backend API for the React frontend application.
## Development Environment


### Local Development Setup
```bash
# Install dependencies
pip install django djangorestframework django-cors-headers

# Database setup
python manage.py makemigrations
python manage.py migrate

# Run development server
python manage.py runserver

# Or for tests run
python manage.py test
```

