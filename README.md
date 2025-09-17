# ✅ TODO Management Application

A modular **Flask + PostgreSQL + SQLAlchemy** backend for managing TODO tasks, following **SOLID principles** and clean architecture.  
The project is designed for scalability, testability, and maintainability, with well-documented setup and development guidelines.

---

## 🚀 Features (Planned)
- User authentication (JWT-based)
- CRUD operations for tasks
- Role-based access control (future)
- Task prioritization & reminders (future)

---

## 🛠 Technology Stack
- **Framework:** Flask 3.0
- **Database:** PostgreSQL 14+
- **ORM:** SQLAlchemy 2.0
- **Migrations:** Alembic
- **Validation:** Pydantic
- **Auth:** Flask-JWT-Extended + Bcrypt
- **Testing:** pytest + pytest-flask + pytest-cov
- **Code Quality:** flake8 + black

---

## 📂 Project Documentation

The project documentation is divided into structured files for clarity:

1. [1_PLANNING.md](./1_PLANNING.md) → Project goals, scope, risks  
2. [2_DESIGN.md](./2_DESIGN.md) → Technology stack & design principles  
3. [3_USER_STORIES.md](./3_USER_STORIES.md) → User roles & stories  
4. [4_API_END_POINTS_OVERVIEW.md](./4_API_END_POINTS_OVERVIEW.md) → API endpoints (request/response)  
5. [5_DATABASE_SCHEMA.md](./5_DATABASE_SCHEMA.md) → Database schema & ERD reference  
6. [6_ARCHITECTURE.md](./6_ARCHITECTURE.md) → System architecture & workflow diagrams  
7. [7_SETUP.md](./7_SETUP.md) → Development setup guide (Git, venv, env vars, DB)  
8. [8_PROJECT_STRUCTURE.md](./8_PROJECT_STRUCTURE.md) → Final folder/file structure  
9. [9_TESTING_SETUP.md](./9_TESTING_SETUP.md) → Testing strategy, coverage, and examples  

---

## ⚡ Quick Start

### 1. Clone Repo
```
git clone git@github.com:Ritika-Bitcot/TODO-Management.git
cd TODO-Management
```

### 2. Setup Environment
```
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3. Configure .env
```
cp .env.example .env
```

Update database and JWT values as needed.

### 4. Run Application
```
python app.py
```

**Visit → http://127.0.0.1:5000/**

You should see:

{"message": "Hello, World!"}

🧪 Run Tests
pytest --cov=app --cov-report=term-missing
