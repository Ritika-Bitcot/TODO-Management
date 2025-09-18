# Design & Technology Stack - TODO Management Application

## 1. Overview
The TODO Management Application is built with a **modular, scalable, and secure architecture**.

The design focuses on:
- **Separation of concerns** (SOLID principles).
- **Scalability** → Easy to extend without modifying existing files.
- **Security-first approach** → JWT, Bcrypt, secure DB access.
- **Maintainability** → Industry-standard frameworks, testing, and CI/CD.

---

## 2. Technology Stack

### 2.1 Programming Language
- **Python 3.12+**
  - Mature, stable, and widely adopted in backend development.
  - Rich ecosystem of libraries (Flask, SQLAlchemy, Pytest).
  - Clear syntax supports maintainability and readability (PEP8).

---

### 2.2 Backend Framework
- **Flask**
  - Lightweight, minimalistic framework with flexibility for modular design.
  - Easy integration with SQLAlchemy ORM, JWT authentication, and middlewares.
  - Excellent for building RESTful APIs.
  - Allows strict adherence to **SOLID principles** since we can design the structure ourselves without heavy conventions.

---

### 2.3 Database
- **PostgreSQL**
  - ACID-compliant relational database.
  - Scales from small to enterprise-level workloads.
  - Strong support for indexing, constraints, and relational integrity.
  - Open-source and well-integrated with Python ORM frameworks.

---

### 2.4 ORM & Migrations
- **SQLAlchemy**
  - Provides abstraction for database operations.
  - Prevents SQL injection via parameterized queries.
  - Maps Python classes to database tables, making code more maintainable.

- **Alembic**
  - Database migration tool.
  - Ensures schema consistency across environments (dev, staging, prod).
  - Enables rollback and versioning for DB schema changes.

---

### 2.5 Authentication & Security
- **JWT (JSON Web Tokens)**
  - Secure, stateless authentication mechanism.
  - Encodes user identity into tokens, eliminating server-side session storage.
  - Supports token expiration, blacklisting (future scope), and scalability in distributed systems.

- **Bcrypt**
  - Industry-standard password hashing.
  - Protects against rainbow table attacks.
  - Configurable salt rounds for stronger security.

---

### 2.6 Testing
- **Pytest**
  - Unit and integration testing framework.
  - Rich plugin ecosystem for database testing, fixtures, and mocking.
  - Supports test-driven development (TDD).

---

### 2.7 Environment & Configuration
- **python-dotenv**
  - Securely loads environment variables (`.env` file).
  - Keeps secrets (DB credentials, JWT secret) out of codebase.

- **Config Layers**
  - Separate configs for development, testing, and production.
  - Adheres to **12-factor app** principles.

---

### 2.8 Deployment & DevOps
- **GitHub (Version Control)**
  - Repository management, pull requests, code reviews.
  - Branching strategy: `main` for production, `dev` for staging, feature branches for new work.

- **GitHub Actions (CI/CD)**
  - Automated testing on pull requests.
  - Ensures code quality before merging.
  - Can be extended to deploy to cloud environments.

- **Docker (Optional, Future Deployment)**
  - Containerization for consistent environments.
  - Useful for scaling across multiple servers or cloud platforms.

---

### 2.9 Code Quality & Standards
- **Flake8** → Enforces PEP8 compliance.
- **Black** → Code formatter for consistency.
- **Pre-commit Hooks** → Run linting and tests before commits.

---

## 3. Design Principles
1. **SOLID Principles**
   - **S**ingle Responsibility → Each module has one clear responsibility (e.g., `auth_service`, `task_service`).
   - **O**pen/Closed → Features are extendable without modifying existing code.
   - **L**iskov Substitution → Interfaces (services) can be extended without breaking client code.
   - **I**nterface Segregation → Controllers use only what they need (e.g., user routes won’t depend on task services).
   - **D**ependency Inversion → High-level modules depend on abstractions, not concrete implementations.

2. **Separation of Concerns**
   - **Routes (Controllers)** → Handle HTTP requests/responses.
   - **Services (Business Logic)** → Core logic of users and tasks.
   - **Models (Data Layer)** → Database schema with SQLAlchemy.
   - **Repositories (Optional Layer)** → Abstract database queries.
   - **Utils (Helpers)** → JWT utilities, password hashing, validation.

3. **Error Handling**
   - Standardized error messages with consistent structure.
   - Maps business logic errors → HTTP response codes (422, 401, 403, 404, 500).

---

## 4. High-Level Design
- **Client** → Makes HTTP requests.
- **Flask API Layer** → Validates input, delegates to services.
- **Service Layer** → Applies business logic, communicates with repository/ORM.
- **Repository Layer** (optional) → Handles raw SQLAlchemy operations.
- **Database Layer (PostgreSQL)** → Stores users and tasks.

---

## 5. Benefits of Chosen Stack
- ✅ **Security** → Bcrypt + JWT + ownership validation.
- ✅ **Scalability** → PostgreSQL + modular Flask structure.
- ✅ **Maintainability** → SOLID + ORM + migrations.
- ✅ **Performance** → Flask is lightweight, PostgreSQL is optimized for queries.
- ✅ **Community Support** → All chosen tools are widely adopted and well-documented.
