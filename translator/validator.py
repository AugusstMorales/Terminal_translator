import re
from typing import Tuple

class InputValidator:
    """Validates user input for translation."""
    @staticmethod
    def validate(text: str) -> Tuple[bool, str]:
        """Check if input is valid for translation."""
        if not text.strip():
            return False, "Input cannot be empty."
        if re.match(r'^[\d\s\W]+$', text):
            return False, "Input should contain meaningful text, not just numbers or symbols."
        return True, ""
