## 1. Validation & Type Safety

Used Pydantic schemas (UserRegisterSchema, UserLoginSchema)

Strong password policy with regex-based validation

Email validation using EmailStr

Prevents weak data entering service or DB layer

## 2. Error Handling

ServiceError custom exception for business logic errors

DB IntegrityError caught & mapped to 409 Conflict

Validation errors return structured 400 with field-specific details

Unexpected errors → 500

## 3. Logging

Structured logging implemented per logger type (app, DB, auth)

Logging levels used consistently:

INFO: successful events (user registered)

WARNING: invalid login attempts

ERROR: failed DB operations

DEBUG: dev mode for tracing payloads

## 4. Security

Passwords hashed with Bcrypt

JWT tokens with expiry & refresh mechanism

No secrets hardcoded (all loaded from .env)

## 5. SOLID Principles

**Single Responsibility** → routes only handle HTTP, services handle business logic

**Open/Closed** → new features added in new files (no breaking old ones)

**Liskov Substitution**→ Service/repository interfaces ensure interchangeable implementations.

**Interface Segregation**→ Separate schemas, services, and repositories so each class does only what it needs.

**Dependency Inversion** → High-level modules depend on abstractions (services) instead of Flask/SQLAlchemy internals.
