from utils.password_helper import PasswordHelper

# Hash a password before saving to DB
hashed = PasswordHelper.hash_password("mysecretpassword")

# Verify login
is_valid = PasswordHelper.verify_password("mysecretpassword", hashed)
