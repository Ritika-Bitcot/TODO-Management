# Authentication APIs
## 1. User Registration

**Endpoint:**

`POST /auth/register`

**Description:**
Registers a new user with unique email and strong password policy.

Request Body (JSON):
```
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "StrongPass@123"
}
```

**Validation Rules:**

**username:** non-empty string

**email:** must be a valid email

**password:**

At least 8 chars

At least 1 uppercase

At least 1 lowercase

At least 1 digit

At least 1 special character

No spaces

**Responses:**

✅ 201 Created
```
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com"
}
```

⚠️ 409 Conflict
```
{ "error": "User with this email already exists" }

```
⚠️ 400 Bad Request
```
{ "errors": [{ "loc": ["password"], "msg": "Weak password" }] }

```
⚠️ 500 Internal Server Error
```
{ "error": "Unexpected error: <details>" }
```
