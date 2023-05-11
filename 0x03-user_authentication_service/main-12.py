#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

session_id = "f454b0aa-a995-457d-85b8-abd6ff0b5c11"
auth = Auth()


print(auth.get_user_from_session_id(session_id))
print(auth.get_user_from_session_id("unknown@email.com"))
print(auth.get_user_from_session_id(None))