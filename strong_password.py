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

validators = [
    [re.compile(r"\S{8,}"), "Make it at least eight characters in length."],
    [re.compile(r"[A-Z]+"), "Include an uppercase letter."],
    [re.compile(r"[a-z]+"), "Add a lowercase letter."],
    [re.compile(r"[\d{1,]"), "Throw in a number or two."],
]


def password_checker() -> list[str]:
    """Prompt user for password, check strength and suggest fixes as needed."""
    checked = check_input(getpass(prompt="Please enter password here: ", stream=None))
    fixes = []
    if 0 not in checked:
        fixes.append("Password passed. Word!")
    else:
        print("Your password is weak. Please consider these tweaks:")
        fixes = [
            f"* {validators[index][1]}"
            for index, check in enumerate(checked)
            if not check
        ]
    return fixes


def check_input(password: str) -> list[bool]:
    """Take in password string, check against regexes
    and return list of bools (True=pass; False=fail)."""
    return [bool(validator[0].search(password)) for validator in validators]


def main() -> None:
    results = password_checker()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
