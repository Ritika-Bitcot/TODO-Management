# System Architecture & Workflows - TODO Management Application

---

## 1. High-Level Architecture

The TODO Management Application follows a **modular, layered architecture** to ensure scalability, maintainability, and security.

### Layers
1. **Client Layer**  
   - Web/Mobile frontend (future integration).  
   - Sends HTTP requests to backend API.  

2. **API Layer (Flask)**  
   - Routes handle HTTP requests & responses.  
   - Input validation and error handling.  
   - Uses JSON for request/response format.  

3. **Service Layer (Business Logic)**  
   - Contains core logic for authentication, user management, and task handling.  
   - Enforces business rules (e.g., ownership validation, status transitions).  

4. **Data Access Layer (ORM / Repositories)**  
   - SQLAlchemy ORM interacts with PostgreSQL.  
   - Alembic manages schema migrations.  

5. **Database Layer (PostgreSQL)**  
   - Stores persistent data: users and tasks.  
   - Enforces relational integrity and constraints.  

6. **Security Layer**  
   - JWT for authentication.  
   - Bcrypt for password hashing.  
   - Role-based access (owner-only for tasks).  

[High Level Diagram](../assests/image-1.png)
---

## 2. Workflows

### 2.1 User Registration & Login

1. Client sends registration request (`POST /auth/register`).  
2. Backend validates email & password → hashes password with Bcrypt.  
3. User is saved in database.  
4. Login request (`POST /auth/login`) validates credentials.  
5. On success, JWT token is generated and returned.  
6. Client stores JWT for authenticated requests.  

[user_register_login diagram ](../assests/image-4.png)
---

### 2.2 Task Workflow

1. Client includes JWT in `Authorization: Bearer <token>`.  
2. Flask middleware validates the token.  
3. Service layer checks if the task belongs to the user.  
4. CRUD operation is performed (Create/Read/Update/Delete).  
5. Response is returned with success/error.  

[workflow diagram](../assests/image-2.png)
---

### 2.3 End-to-End Workflow

1. Client → Flask API Layer  
2. API Layer → Service Layer (business logic)  
3. Service Layer → Data Access Layer (ORM)  
4. Data Access Layer → PostgreSQL DB  
5. PostgreSQL → returns data → Service Layer → API Layer → Client  

[end_to_end workflow diagram](../assests/image-3.png)
---

## 3. ER Diagram

Below is the conceptual ER diagram:
[ER Diagram](../assests/image.png)