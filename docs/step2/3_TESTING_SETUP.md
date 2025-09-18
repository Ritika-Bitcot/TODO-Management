# Testing Setup - TODO Management Application

Testing ensures code quality, correctness of business logic, and security compliance.
The application uses **pytest** as the testing framework with **pytest-flask** for Flask integration.

---

## 1. Testing Framework & Dependencies
Install dependencies (already in `requirements.txt`):
```
pip install pytest pytest-flask pytest-cov
```
pytest → Base testing framework

pytest-flask → Provides client fixture to test Flask endpoints

pytest-cov → Generates coverage reports

## 2. Test Types

We will test all critical components:

### Routes (Controllers)

Verify HTTP request/response handling.

Validate correct status codes and response formats.

### Services (Business Logic)

Test user registration/login logic.

Test task creation/update/delete rules (ownership validation, status changes).

### Models (SQLAlchemy ORM)

Test model constraints (e.g., unique email, status ENUM).

Test cascade delete (user → tasks).

### Utils (Helpers)

Test JWT generation/validation.

Test Bcrypt password hashing and validation.

### Integration Tests

End-to-end flows: registration → login → task CRUD.

Ensure database + services + routes work together.

### Security Tests

Invalid/expired JWT tokens.

Unauthorized task access.

SQL injection attempts.

## 3. Test Configuration

Create ```pytest.ini``` in the project root:
```
[pytest]
testpaths = tests
addopts = --cov=app --cov-report=term-missing -v
```

Runs all tests inside ```tests/```.

Prints missing coverage lines.

Uses verbose mode for better output.

## 4. Folder Structure for Tests
```
tests/
│
├── __init__.py
├── test_auth_routes.py       # /auth endpoints
├── test_task_routes.py       # /tasks endpoints
├── test_auth_service.py      # Business logic for users
├── test_task_service.py      # Business logic for tasks
├── test_utils.py             # JWT + password helpers
├── test_models.py            # User & Task models
└── conftest.py               # Common pytest fixtures
```
## 5. Running Tests

### Run all tests:
```
pytest
```

### Run with coverage:
```
pytest --cov=app --cov-report=term-missing
```
## 6. CI/CD Integration

GitHub Actions workflow (```.github/workflows/tests.yml```) already provided in setup docs.

Runs tests on every push/PR.

Uses a PostgreSQL service container.

Blocks merging if tests fail.

## 9. Success Criteria

✅ All unit, integration, and security tests pass.

✅ Minimum 80% code coverage across routes, services, utils, and models.

✅ Unauthorized access attempts always return correct error codes (401/403).
