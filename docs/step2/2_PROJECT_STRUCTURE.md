# Project Structure - TODO Management Application

The project follows **SOLID principles** and a **layered architecture** for scalability and maintainability.
Every feature is implemented in its own module, ensuring that new functionality can be added without modifying existing files.

---

## 1. Folder Structure
```
TODO-Management/
│
├── docs/
│   ├── assests/
│   │   ├──image-1.png
│   │   ├──image-2.png
│   │   └──image-3.png
│   │   └──image-4.png
│   │   └──image.png
│   │
│   ├── step1/
│   │   ├──1_PLANNING.md
│   │   ├──2_DESIGN.md
│   │   └──3_USER_STORIES.md
│   │   └──4_API_END_POINTS_OVERVIEW.md
│   │   └──5_DATABASE_SCHEMA.md
│   │   └──6_ARCHITECTURE.md
│   │
|   ├── step2/
│   │   ├──1_SETUP.md
│   │   ├──2_PROJECT_STRUCTURE.md
│   │   └──3_TESTING_SETUP.md
│   │
├── requirements/
│   └── requirements.txt
│   │
├── src/
│   ├── __init__.py             # (empty by requirement)
│   ├── config.py               # Configurations for envs
│   ├── constant.py             # Shared constants (like status values)
│   │
│   ├── routes/                 # Controllers
│   │   ├── __init__.py         # (empty)
│   │   ├── register.py
│   │   └── home_routes.py      # Placeholder
│   │   ├── auth_routes.py      # Placeholder
│   │   └── task_routes.py      # Placeholder
│   │
│   ├── services/               # Business logic
│   │   ├── __init__.py         # (empty)
│   │   ├── auth_service.py     # Placeholder
│   │   └── task_service.py     # Placeholder
│   │
│   ├── models/                 # Database models
│   │   ├── __init__.py         # (empty)
│   │   ├── user_model.py       # Placeholder
│   │   └── task_model.py       # Placeholder
│   │
│   ├── repositories/           # Data access (optional layer)
│   │   ├── __init__.py         # (empty)
│   │   ├── user_repository.py  # Placeholder
│   │   └── task_repository.py  # Placeholder
│   │
│   ├── utils/                  # Helpers
│   │   ├── __init__.py         # (empty)
│   │   ├── jwt_helper.py       # Placeholder
│   │   └── password_helper.py  # Placeholder
│   │
│   ├── schemas/                # Validation schemas
│   │   ├── __init__.py         # (empty)
│   │   ├── user_schema.py      # Placeholder
│   │   └── task_schema.py      # Placeholder
│   │
│   ├── migrations/             # Alembic (init later)
│   │   └── versions/           # Migration scripts
│   │
│   └── tests/                  # Test cases
│       ├── __init__.py         # (empty)
│       ├── test_auth.py        # Placeholder
│       └── test_task.py        # Placeholder
│
├── .env.example                # Example env file
├── .gitignore                  # Ignore venv, pycache, etc.
├── CHANGELOG.md
├── .pre-commit-config.yaml
├── alembic.ini                 # Alembic configuration (after init)
├── app.py                      # Flask entry point
└── README.md                   # Project overview
```
---

## 2. SOLID Principle Mapping
- **S**ingle Responsibility → Each layer (routes, services, models) has its own responsibility.
- **O**pen/Closed → New features are added as new files, existing ones remain unchanged.
- **L**iskov Substitution → Services can be extended with inheritance without breaking existing code.
- **I**nterface Segregation → Routes only depend on the service methods they need.
- **D**ependency Inversion → High-level modules (routes) depend on service abstractions, not implementations.

---

## 3. Advantages
- Clear separation of concerns.
- Easy to test each module independently.
- Scalable for future features (tags, reminders, priorities).
