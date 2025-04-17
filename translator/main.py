from .ui import UI
from .translator import Translator
from .validator import InputValidator
from .config import AppConfig

class TranslatorApp:
    """Main application class for the translator."""
    def __init__(self):
        self.ui = UI()
        self.validator = InputValidator()

    def run(self):
        """Run the translator application."""
        self.ui.display_welcome()
        
        # Choose translation direction
        source_code, target_code = self.ui.prompt_translation_direction()
        source_lang = next(lang.name for lang in AppConfig.SUPPORTED_LANGUAGES if lang.code == source_code)
        target_lang = next(lang.name for lang in AppConfig.SUPPORTED_LANGUAGES if lang.code == target_code)
        direction = f"{source_lang} to {target_lang}"
        
        translator = Translator(source_code, target_code)
        self.ui.display_ready_message(direction)
        
        # Main loop
        while True:
            text = self.ui.prompt_text(source_lang)
            
            if text.lower() == "exit":
                self.ui.display_exit_message()
                break
            
            # Validate input
            is_valid, error_msg = self.validator.validate(text)
            if not is_valid:
                self.ui.display_error(error_msg)
                continue
            
            # Translate and display
            self.ui.display_translating()
            translated = translator.translate(text)
            self.ui.display_translation(text, translated, source_lang, target_lang)
