#!/usr/bin/env python3
# strong_password.py — An exercise in understanding regular expressions.
# For more information, see README.md

from getpass import getpass
import logging
import re

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def passcheck(password):
    passlength = re.compile(r"\S{8,}")
    passupper = re.compile(r"[A-Z]+")
    passlower = re.compile(r"[a-z]+")
    passnumber = re.compile(r"[\d{1,]")

    if passlength.search(password) == None:
        print(f"Password must contain at least eight characters.")
    elif passupper.search(password) == None:
        print(f"Password must contain at least one capital letter.")
    elif passlower.search(password) == None:
        print(f"Password must contain at least one lowercase letter.")
    elif passnumber.search(password) == None:
        print(f"Password must contain at least one number.")
    else:
        return password


print(
    f"""A valid password must be at least eight characters long and contain at least
one uppercase letter, one lowercase letter and one number."""
)
user_password = getpass(prompt="Password: ", stream=None)
passcheck(user_password)
