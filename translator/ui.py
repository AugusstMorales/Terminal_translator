from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from .config import UIStyle, AppConfig

class UI:
    """Manages the user interface with an Apple-like design."""
    def __init__(self):
        self.console = Console()

    def display_welcome(self):
        """Display the welcome message in a stylish panel."""
        self.console.print(Panel(
            Text(AppConfig.WELCOME_MESSAGE, style=UIStyle.PRIMARY_COLOR, justify="center"),
            title="Translator",
            subtitle="Minimalist & Elegant",
            style=UIStyle.PRIMARY_COLOR,
            border_style=UIStyle.PANEL_BORDER,
            padding=UIStyle.PADDING
        ))

    def prompt_translation_direction(self):
        """Prompt user to select translation direction."""
        self.console.print(Text("Choose translation direction:", style=f"italic {UIStyle.ACCENT_COLOR}"))
        for i, lang in enumerate(AppConfig.SUPPORTED_LANGUAGES, 1):
            target_lang = AppConfig.SUPPORTED_LANGUAGES[1 - i]
            self.console.print(f"  [{i}] {lang.name} to {target_lang.name}")
        choice = Prompt.ask(
            f"Enter [{1}] or [{2}]",
            choices=["1", "2"],
            default="1"
        )
        return (AppConfig.SUPPORTED_LANGUAGES[0].code, AppConfig.SUPPORTED_LANGUAGES[1].code) if choice == "1" else (AppConfig.SUPPORTED_LANGUAGES[1].code, AppConfig.SUPPORTED_LANGUAGES[0].code)

    def display_ready_message(self, direction: str):
        """Display ready-to-translate message."""
        self.console.print(Panel(
            f"Ready to translate from {direction}. Type 'exit' to quit.",
            style=UIStyle.PRIMARY_COLOR,
            border_style=UIStyle.PANEL_BORDER,
            padding=UIStyle.PADDING
        ))

    def prompt_text(self, source_lang: str):
        """Prompt for text to translate."""
        return Prompt.ask(f"[bold {UIStyle.PRIMARY_COLOR}]Text to translate ({source_lang})[/bold {UIStyle.PRIMARY_COLOR}]")

    def display_translation(self, original: str, translated: str, source_lang: str, target_lang: str):
        """Display translation in a clean table."""
        table = Table(show_header=False, box=UIStyle.TABLE_BOX, style=UIStyle.SECONDARY_COLOR)
        table.add_column(style=UIStyle.PRIMARY_COLOR, justify="left")
        table.add_column(style=UIStyle.ACCENT_COLOR, justify="left")
        table.add_row(source_lang, original)
        table.add_row(target_lang, translated)
        
        self.console.print(Panel(
            table,
            border_style=UIStyle.PANEL_BORDER,
            padding=UIStyle.PADDING,
            style=UIStyle.PRIMARY_COLOR
        ))

    def display_error(self, message: str):
        """Display error message in a red panel."""
        self.console.print(Panel(
            Text(message, style=f"bold {UIStyle.ERROR_COLOR}", justify="center"),
            style=UIStyle.ERROR_COLOR,
            border_style=UIStyle.ERROR_COLOR,
            padding=UIStyle.PADDING
        ))

    def display_translating(self):
        """Display translating status."""
        self.console.print(Text("Translating...", style=f"italic {UIStyle.SECONDARY_COLOR}"))

    def display_exit_message(self):
        """Display exit message."""
        self.console.print(Panel(
            Text(AppConfig.EXIT_MESSAGE, style=UIStyle.PRIMARY_COLOR, justify="center"),
            style=UIStyle.PRIMARY_COLOR,
            border_style=UIStyle.PANEL_BORDER,
            padding=UIStyle.PADDING
        ))
