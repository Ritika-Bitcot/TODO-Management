# User Stories with Acceptance Criteria - TODO Management Application

---

## 1. User Registration
**User Story:**
As a new user, I want to register with a unique email and a strong password so that I can create an account and manage my tasks.

**Preconditions:**
- User does not already exist in the database.

**Acceptance Criteria:**
- ✅ Email must be in a valid format (e.g., user@example.com).
- ✅ Password must meet strong password rules:
  - Minimum 8 characters
  - At least 1 uppercase letter
  - At least 1 lowercase letter
  - At least 1 number
- ✅ Registration fails if the email already exists (`400 Bad Request`).
- ✅ Passwords must be stored in a **hashed format** using Bcrypt.
- ✅ On success, API returns `201 Created` with a success message.

**Postconditions:**
- User record is created in `users` table.
- User can log in using provided credentials.

**Edge Cases:**
- Invalid email → `422 Unprocessable Entity`
- Weak password → `422 Unprocessable Entity`

---

## 2. User Login
**User Story:**
As a registered user, I want to log in with my email and password so that I can obtain a JWT token to access my tasks securely.

**Preconditions:**
- User must already exist in the database with valid credentials.

**Acceptance Criteria:**
- ✅ Validate email and password against stored hashed password.
- ✅ Return `401 Unauthorized` if credentials are invalid.
- ✅ On success, return `200 OK` with:
  - `access_token` (JWT)
  - `token_type = bearer`
- ✅ JWT should include user’s unique identifier (`user_id`).
- ✅ JWT should expire after a configurable duration (default: 1 hour).

**Postconditions:**
- Client stores the JWT and includes it in the Authorization header for future requests.

**Edge Cases:**
- Wrong password → `401 Unauthorized`
- Expired token used later → `401 Unauthorized`

---

## 3. Create TODO Task
**User Story:**
As a logged-in user, I want to create a TODO task so that I can track my activities.

**Preconditions:**
- User must be authenticated with a valid JWT.

**Acceptance Criteria:**
- ✅ Only authenticated users can create tasks.
- ✅ Task must include a **title** (required).
- ✅ Optional fields: description, due_date (must be a valid date format).
- ✅ Each task must be associated with the logged-in user (owner_id).
- ✅ On success, return `201 Created` with task details.

**Postconditions:**
- New task record created in `tasks` table linked to the owner_id.

**Edge Cases:**
- Missing title → `422 Unprocessable Entity`

---

## 4. View TODO Tasks
**User Story:**
As a logged-in user, I want to view my tasks so that I can monitor my activities.

**Preconditions:**
- User must be authenticated with a valid JWT.

**Acceptance Criteria:**
- ✅ `GET /tasks` returns all tasks belonging to the logged-in user.
- ✅ `GET /tasks/{task_id}` returns only if the task belongs to the logged-in user.
- ✅ If user tries to view another user’s task → `403 Forbidden`.
- ✅ If task doesn’t exist → `404 Not Found`.

**Postconditions:**
- User sees only their own tasks.

**Edge Cases:**
- Empty task list → Return empty array `[]`.
- Task id not found → `404 Not Found`.
---

## 5. Update TODO Task
**User Story:**
As a logged-in user, I want to update my tasks so that I can modify task details.

**Preconditions:**
- User must be authenticated with a valid JWT.
- Task must exist and belong to the user.

**Acceptance Criteria:**
- ✅ Allowed updates: `title`, `description`, `due_date`, `status`.
- ✅ Status transitions should be valid (e.g., pending → in_progress → completed).
- ✅ Invalid formats (e.g., invalid date) must be rejected.
- ✅ On success, return `200 OK` with updated task details.
- ✅ If task does not belong to user → `403 Forbidden`.

**Postconditions:**
- Task record updated in database.

**Edge Cases:**
- Invalid date format → `422 Unprocessable Entity`

---

## 6. Delete TODO Task
**User Story:**
As a logged-in user, I want to delete my tasks so that I can remove tasks I no longer need.

**Preconditions:**
- User must be authenticated with a valid JWT.
- Task must exist and belong to the user.

**Acceptance Criteria:**
- ✅ Only authenticated users can delete tasks.
- ✅ Users can delete only their own tasks.
- ✅ On success, return `200 OK` with a confirmation message.
- ✅ If task does not exist → `404 Not Found`.
- ✅ If task belongs to another user → `403 Forbidden`.

**Postconditions:**
- Task record removed from `tasks` table.

**Edge Cases:**
- Task already deleted → `404 Not Found`.
- Trying to delete another user’s task → `403 Forbidden`.
