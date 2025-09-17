# API Endpoints Overview - TODO Management Application

This document describes all API endpoints, their request/response formats, authentication requirements, and error handling.

---

## 1. Authentication Endpoints

### **Register User**
- **Endpoint:** `/auth/register`  
- **Method:** `POST`  
- **Auth Required:** ❌ No  
- **Description:** Register a new user with email and password.

#### Request Body
```
{
  "email": "user@example.com",
  "password": "Secret123"
}
```
#### Success Response (201 Created)
```
{
  "message": "User registered successfully"
}
```
#### Error Responses
```
400 Bad Request → Email already registered

422 Unprocessable Entity → Invalid email or weak password
```
### **Login User**

**Endpoint:** /auth/login

**Method:** POST

**Auth Required:** ❌ No

**Authenticate:** a user and return a JWT token.

#### Request Body
```
{
  "email": "user@example.com",
  "password": "Secret123"
}
```
#### Success Response (200 OK)
```
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```
#### Error Responses
```
401 Unauthorized → Invalid email or password
```

## 2. Task Endpoints
### **List Tasks**

**Endpoint:** ```/tasks```

**Method:** GET

**Auth Required:** ✅ Yes (JWT)

**Description:** Retrieve all tasks for the logged-in user.

#### Success Response (200 OK)
```
[
  {
    "id": 1,
    "title": "Buy milk",
    "description": "2 liters",
    "due_date": "2025-09-20",
    "status": "pending",
    "owner_id": 1
  },
  {
    "id": 2,
    "title": "Finish project",
    "description": "Due by Friday",
    "due_date": "2025-09-18",
    "status": "in_progress",
    "owner_id": 1
  }
]
```
#### Error Responses
```
401 Unauthorized → Missing or invalid token
```

### Create Task

**Endpoint:** ```/tasks```

**Method:** POST

**Auth Required:** ✅ Yes (JWT)

**Description:** Create a new task for the logged-in user.

#### Request Body
```
{
  "title": "Buy groceries",
  "description": "Fruits and vegetables",
  "due_date": "2025-09-22"
}
```

#### Success Response (201 Created)
```
{
  "id": 3,
  "title": "Buy groceries",
  "description": "Fruits and vegetables",
  "due_date": "2025-09-22",
  "status": "pending",
  "owner_id": 1
}
```
#### Error Responses
```
422 Unprocessable Entity → Missing title or invalid due_date
```
### Retrieve Single Task

**Endpoint:** ```/tasks/{task_id}```

**Method:** GET

**Auth Required:** ✅ Yes (JWT)

**Description:** Retrieve a single task by ID (only if owned by user).

#### Success Response (200 OK)
```
{
  "id": 3,
  "title": "Buy groceries",
  "description": "Fruits and vegetables",
  "due_date": "2025-09-22",
  "status": "pending",
  "owner_id": 1
}
```
#### Error Responses
```
403 Forbidden → Task does not belong to user

404 Not Found → Task does not exist
```

### Update Task

**Endpoint:** ```/tasks/{task_id}```

**Method:** PUT

**Auth Required:** ✅ Yes (JWT)

**Description:** Update task details (only if owned by user).

#### Request Body
```
{
  "title": "Buy groceries",
  "description": "Fruits, vegetables, and milk",
  "due_date": "2025-09-23",
  "status": "in_progress"
}
```
#### Success Response (200 OK)
```
{
  "id": 3,
  "title": "Buy groceries",
  "description": "Fruits, vegetables, and milk",
  "due_date": "2025-09-23",
  "status": "in_progress",
  "owner_id": 1
}
```
#### Error Responses
```
403 Forbidden → Task does not belong to user

404 Not Found → Task does not exist

422 Unprocessable Entity → Invalid data format
```
### Delete Task

**Endpoint:** ```/tasks/{task_id}```

**Method:** DELETE

**Auth Required:** ✅ Yes (JWT)

**Description:** Delete a task (only if owned by user).

#### Success Response (200 OK)
```
{
  "message": "Task deleted successfully"
}
```
#### Error Responses
```
403 Forbidden → Task does not belong to user

404 Not Found → Task does not exist
```

## 3. Error Handling Standards

All error responses follow a consistent JSON format:
```
{
  "detail": "Error message here"
}
```

|**HTTP Code** | **Example Message**    |
| --------- | -------------------------- |
| 400       | "Email already registered" |
| 401       | "Invalid or expired token" |
| 403       | "You do not have access"   |
| 404       | "Task not found"           |
| 422       | "Invalid request format"   |
| 500       | "Internal server error"    |
