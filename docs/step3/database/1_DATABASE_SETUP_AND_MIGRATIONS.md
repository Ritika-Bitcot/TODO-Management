# 🗄️ Database Setup & Migrations

## 1. **Database Setup**
We are using **PostgreSQL** with **SQLAlchemy ORM** and **Alembic** for migrations.

### Steps:
1. **Install PostgreSQL**
   ```
   sudo apt update
   sudo apt install postgresql postgresql-contrib
   ```
2. **Create Database & User**
```
sudo -u postgres psql
CREATE DATABASE todo_management;
CREATE USER todo_user WITH PASSWORD 'yourpassword';
ALTER ROLE todo_user SET client_encoding TO 'utf8';
ALTER ROLE todo_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE todo_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE todo_management TO todo_user;
\q
```
3. **Configure .env**
```
DATABASE_URL=postgresql+psycopg2://todo_user:yourpassword@localhost/todo_management
```

4. **Test Connection**
```
python -m src.app
```

## 2. **Migrations with Alembic**

We use Alembic for managing schema changes.

**Initialize Alembic**
```
alembic init migrations
```

This creates a `migrations/ folder`.
```
Update alembic.ini
```
**Set the database URL:**
```
sqlalchemy.url = postgresql+psycopg2://todo_user:yourpassword@localhost/todo_management
```
**Autogenerate a Migration**
Whenever models change:
```
alembic revision --autogenerate -m "create users and tasks tables"
```
**Apply Migrations**
```
alembic upgrade head
```
**Rollback Migration**
```
alembic downgrade -1
```
**Example Migration Script**

Located in migrations/versions/xxxxxxxx_create_users.py:
```
def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String, nullable=False, unique=True),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("password_hash", sa.String, nullable=False),
    )

def downgrade():
    op.drop_table("users")
```
## 3. **Best Practices**

✅ Keep .env secret; don’t hardcode DB credentials.

✅ Always run alembic revision --autogenerate after modifying models.

✅ Run alembic upgrade head on staging before production.

✅ Never manually edit the database schema in production.
