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

regexes = [
    re.compile(r"\S{8,}"),
    re.compile(r"[A-Z]+"),
    re.compile(r"[a-z]+"),
    re.compile(r"[\d{1,]"),
]

fixes = [
    "Make it at least eight characters in length.",
    "Include an uppercase letter.",
    "Add a lowercase letter.",
    "Throw in a number or two.",
]


def main() -> None:
    """Prompt user for password, check strength and suggest fixes as needed."""
    checked = pass_check(getpass(prompt="Please enter password here: ", stream=None))
    if 0 not in checked:
        print("Password passed. Word!")
    else:
        print("Your password is weak. Please consider these tweaks:")
        for index, check in enumerate(checked):
            if not check:
                print(f"* {fixes[index]}")


def pass_check(password: str) -> list[bool]:
    """Take in password string, check against regexes
    and return list of bools (True=pass; False=fail)."""
    return [bool(validator.search(password)) for validator in regexes]


if __name__ == "__main__":
    main()
