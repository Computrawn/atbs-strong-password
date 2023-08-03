# python3
"""
Prepared for hub. Needs refactor.
"""

import re


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
user_password = input("Please enter your password: ")
passcheck(user_password)
