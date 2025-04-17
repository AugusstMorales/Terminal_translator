import sys
from translator.main import TranslatorApp

def main():
    """Run the Translator application."""
    app = TranslatorApp()
    try:
        app.run()
    except KeyboardInterrupt:
        app.ui.display_exit_message()
    except Exception as e:
        app.ui.display_error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
