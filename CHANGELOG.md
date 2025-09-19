# Changelog

## [Step 3]

**Password Security**

### Added

- `src/utils/password_helper.py` for bcrypt hashing and verification of passwords.
- `src/services/auth_service.py` integration with Password Helper for user register and password verfy.

**Database Integration & Migration**
### Added

- SQLAlchemy integration and database connection setup in src/core/database.py
- Alembic configuration (alembic.ini) and initial migration folder (src/migrations/)
- Database models for User and Task, including base.py for shared metadata

### Changed
- Moved config from src/config.py → src/core/config.py (as part of new core/ structure)
- Updated `.pre-commit-config.yaml` to ignore updating migrations
- Updated `src/app.py` to change path for `config.py` import
- Updated project structure documentation (docs/step2/2_PROJECT_STRUCTURE.md) to reflect database layer

**Local Development Setup**
### Added
- Local development setup with environment-based configuration
- `.env` and `.env.example` for Flask secret key, DB URL, and JWT secret
- Validation of environment variables using **Pydantic** in `src/config.py`

## [Step 2]
### Added
- Project setup guide, project structure, and testing documentation
- `.env.example`, `.pre-commit-config.yaml`, `requirements.txt` and requirements folder
- Initial Flask app with routes and welcome GET endpoint
- `src/` folder for future modules

### Changed
- Restructured `docs/step2` with renamed files for clarity
- `.gitignore` updated to ignore pycache and Python build artifacts

### Removed
- Old setup, project structure, and testing docs from `docs/step2`
- Old `app/__init__.py` and route files replaced by new structure

## [Step 1]

### Added
- Planning, design, user stories
- API endpoints overview
- Database schema
- Architecture documentation

### Changed
- Updated architecture documentation with corrected references

### Removed
- `__pycache__` and Python build artifacts removed from repository
