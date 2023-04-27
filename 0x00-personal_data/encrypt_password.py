#!/usr/bin/env python3
"""
Password encryption using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password as a byte string
    """
    # Encode the password string
    encoded_password = password.encode()

    # Generate a salt and hash the encoded password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)

    # Return the hashed password
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password
    """
    # Encode the password string
    encoded_password = password.encode()

    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(encoded_password, hashed_password)
