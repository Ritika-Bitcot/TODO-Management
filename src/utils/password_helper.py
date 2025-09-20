from bcrypt import checkpw, gensalt, hashpw


class PasswordHelper:
    """Utility class for hashing and verifying passwords using bcrypt."""

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a plain-text password.

        Args:
            password (str): The plain-text password to hash.

        Returns:
            str: The hashed password (utf-8 string).
        """
        if not password:
            raise ValueError("Password cannot be empty")

        hashed = hashpw(password.encode("utf-8"), gensalt())
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """
        Verify a plain-text password against a hashed password.

        Args:
            password (str): The plain-text password.
            hashed_password (str): The previously hashed password.

        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        if not password or not hashed_password:
            return False
        return checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
