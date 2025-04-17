from typing import NamedTuple
from rich.box import SIMPLE

class LanguageConfig(NamedTuple):
    """Configuration for source and target languages."""
    code: str
    name: str

class UIStyle:
    """Centralized UI styling configuration."""
    PRIMARY_COLOR = "white"
    ACCENT_COLOR = "cyan"
    ERROR_COLOR = "red"
    SECONDARY_COLOR = "bright_black"
    TABLE_BOX = SIMPLE
    PANEL_BORDER = "bright_black"
    PADDING = (1, 2)

class AppConfig:
    """Application configuration."""
    SUPPORTED_LANGUAGES = [
        LanguageConfig(code="en", name="English"),
        LanguageConfig(code="es", name="Spanish"),
    ]
    DEFAULT_SOURCE = "en"
    DEFAULT_TARGET = "es"
    WELCOME_MESSAGE = "Welcome to Translator"
    EXIT_MESSAGE = "Thank you for using Translator!"
