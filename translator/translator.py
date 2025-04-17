from deep_translator import GoogleTranslator

class Translator:
    """Handles translation logic."""
    def __init__(self, source: str, target: str):
        self.translator = GoogleTranslator(source=source, target=target)

    def translate(self, text: str) -> str:
        """Translate text and handle errors."""
        try:
            return self.translator.translate(text)
        except Exception as e:
            return f"Translation error: {e}"
