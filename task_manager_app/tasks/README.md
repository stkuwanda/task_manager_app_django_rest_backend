# Task Manager App Documentation

The `tasks` app is the core Django application that handles all task-related functionality, user management, and API endpoints. This app implements the business logic layer between the database models and the REST API interface.

## Overview

This Django app provides a complete task management system with user authentication, CRUD operations, and proper data validation. It uses Django REST Framework to expose clean, RESTful API endpoints that the frontend React application consumes.


## API Views

### TaskViewSet
The main API interface uses Django REST Framework's ModelViewSet pattern:

**Endpoints:**
- `GET /api/tasks/` - List all tasks for authenticated user
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a specific task
- `PUT /api/tasks/{id}/` - Update a task completely
- `PATCH /api/tasks/{id}/` - Partial task update
- `DELETE /api/tasks/{id}/` - Delete a task

**Security Features:**
- Token authentication required for all operations
- Users can only access their own tasks
- Automatic owner assignment on task creation
- Proper permission checking on all operations

### SignupView
Custom API view for user registration:

**Endpoint:** `POST /api/auth/signup/`

**Functionality:**
- Creates new user accounts
- Generates authentication tokens
- Validates user input data
- Returns token for immediate authentication

## Authentication System

### Token Authentication
The app uses Django REST Framework's token authentication:

**Implementation:**
1. Users receive tokens upon registration or login
2. Tokens must be included in API request headers
3. Format: `Authorization: Token <token_value>`
4. Tokens persist until manually revoked

**Security Considerations:**
- Tokens are stored securely in the database
- Each user has a unique token
- Missing or invalid tokens result in 401 responses
- Proper CORS configuration for frontend integration

## Testing

The app includes comprehensive test coverage:

### Test Categories
1. **Model Tests**: Validate data integrity and relationships
2. **API Tests**: Test all CRUD operations and edge cases
3. **Authentication Tests**: Verify security and access control

### Key Test Scenarios
- Authentication and authorization flows
- CRUD operations with proper status codes