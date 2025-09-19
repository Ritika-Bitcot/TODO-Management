import re
from typing import Annotated

from pydantic import BaseModel, EmailStr, constr, field_validator


class UserRegisterSchema(BaseModel):
    """Schema for validating user registration input with strong password policy."""

    username: str
    email: EmailStr
    password: Annotated[str, constr(min_length=8)]

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, value: str) -> str:
        """Ensure password is strong."""
        pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[^\s]{8,}$")
        if not pattern.match(value):
            raise ValueError(
                "Password must be at least 8 characters, include one uppercase "
                "letter, one lowercase letter, one number, one special character, "
                "and have no spaces."
            )
        return value


class UserLoginSchema(BaseModel):
    """Schema for validating user login input."""

    email: EmailStr
    password: str
