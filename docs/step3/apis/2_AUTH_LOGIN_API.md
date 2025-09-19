# 2. User Login

**Endpoint:**

`POST /auth/login`


**Description:**
Authenticates user and returns JWT access & refresh tokens.

**Request Body (JSON):**
```
{
  "email": "john@example.com",
  "password": "StrongPass@123"
}
```

**Responses:**

✅ 200 OK
```
{
  "access_token": "<JWT_ACCESS_TOKEN>",
  "refresh_token": "<JWT_REFRESH_TOKEN>"
}
```

⚠️ 401 Unauthorized
```
{ "error": "Invalid credentials" }
```

⚠️ 400 Bad Request
```
{ "errors": [{ "loc": ["email"], "msg": "value is not a valid email" }] }
```

⚠️ 500 Internal Server Error
```
{ "error": "Unexpected error: <details>" }
```
