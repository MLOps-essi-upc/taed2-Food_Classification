""""
This script checks Python Version Compatibility 
and raises exceptions if there's a mismatch.
"""

import sys

REQUIRED_PYTHON = "python3"


def main():
    """Check Python version compatibility."""

    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError(f"Unrecognized python interpreter: {REQUIRED_PYTHON}")

    if system_major != required_major:
        raise TypeError(
            f"This project requires Python {required_major}. "
            f"Found: Python {sys.version_info.major}"
        )

    print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
