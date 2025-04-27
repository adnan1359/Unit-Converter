"""
Performs input validation
"""

def validate_input(input: float) -> None:
    if input < 0:
        raise ValueError("Length cannot be negative")