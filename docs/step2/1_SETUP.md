# Project Setup Guide - TODO Management Application

This document provides a step-by-step guide to set up the backend development environment for the TODO Management Application.

---

## 1. Prerequisites
Ensure you have the following installed:
- **Python 3.12+**
- **PostgreSQL 14+**
- **Git**
- **pip** (Python package manager)
- **virtualenv** (for isolated environments)
- **Docker** (optional, for containerized deployments)

---

## 2. Repository Setup

### 1. Clone the repository:
```
git clone git@github.com:Ritika-Bitcot/TODO-Management.git
cd TODO-Management
```
### Setup development branch:
```
git checkout -b dev
```

### 3. Virtual Environment & Dependencies

Create virtual environment:
```
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### Install dependencies from requirements.txt:
```
pip install -r requirements.txt
```

Freeze dependencies (if adding new packages):
```
pip freeze > requirements.txt
```
### 4. Environment Variables

Copy .env.example to .env:
```
cp .env.example .env
```

### Update .env values as needed:

-Database username, password, host, port

-Flask secret key

-JWT secret & expiry

### 5. Database Setup

#### Create PostgreSQL user and database:
```
CREATE USER todo_user WITH PASSWORD 'securepassword';
CREATE DATABASE todo_db OWNER todo_user;
```

#### Apply Alembic migrations (later when models are ready):
```
alembic upgrade head
```

### 6. Running the Application

Run Flask server:
```
flask run
```

By default, the API will be available at:
```
http://127.0.0.1:5000
```

### 7. Git Workflow

We follow feature branch workflow:

```main``` → production branch

```devlop``` → integration branch (latest tested code)

```feature/<feature-name>``` → for each new feature

Example:
```
git checkout -b feature/authentication
```
# implement feature
```
git push origin feature/authentication
```

Then open a Pull Request into ```develop```.

8. Deliverables

✅ requirements.txt → Dependencies file

✅ .env.example → Helps developers create .env

✅ PostgreSQL setup ready

✅ Flask app running locally
