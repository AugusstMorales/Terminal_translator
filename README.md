# Translator

A minimalist, elegant terminal-based translation tool for seamless English-Spanish translations.

## Overview

Translator is a lightweight command-line application designed to provide fast and intuitive translations between English and Spanish. With a sleek, Apple-inspired interface, it offers a delightful user experience while maintaining low resource usage. Whether you're translating a single phrase or engaging in a bilingual conversation, Translator ensures accuracy and simplicity.

### Key Features
- **Bidirectional Translation**: Translate from English to Spanish or Spanish to English with a single command.
- **Elegant Interface**: Clean, modern design with intuitive prompts and visually appealing output.
- **Robust Error Handling**: Gracefully manages invalid inputs and network issues.
- **Optimized Performance**: Minimal resource consumption for efficient operation.
- **Modular Architecture**: Professional, scalable codebase for easy maintenance and extension.

## Technologies

Translator is built with modern Python technologies, ensuring reliability and performance:

- **Python 3.13**: The core programming language, chosen for its versatility and robust standard library.
- **Rich**: A Python library for creating beautiful, formatted terminal output with tables and panels.
- **Deep Translator**: A reliable library for accessing Google Translate's API, providing accurate translations.
- **Regular Expressions (re)**: Used for input validation to ensure meaningful text submissions.

## Dependencies

To run Translator, you'll need the following Python packages:

| Package          | Version  | Purpose                              |
|------------------|----------|--------------------------------------|
| `deep-translator`| Latest   | Handles translation via Google Translate |
| `rich`           | Latest   | Provides elegant terminal formatting  |

## Getting Started

Follow these steps to set up and run Translator on your system.

### Prerequisites
- **Python 3.13** or later installed. Verify with:
  ```bash
  python --version
  ```
- A stable internet connection for translation services.
- A terminal emulator (e.g., Terminal on macOS, Command Prompt on Windows, or any Linux terminal).

### Installation
1. **Clone or Download the Project**
   - If using Git, clone the repository:
     ```bash
     git clone <repository-url>
     cd translate_terminal
     ```
   - Alternatively, download and extract the project files.

2. **Set Up a Virtual Environment**
   - Create a virtual environment to isolate dependencies:
     ```bash
     python -m venv traductor_env
     ```
   - Activate the virtual environment:
     - On macOS/Linux:
       ```bash
       source traductor_env/bin/activate
       ```
     - On Windows:
       ```bash
       traductor_env\Scripts\activate
       ```

3. **Install Dependencies**
   - Install the required packages:
     ```bash
     pip install deep-translator rich
     ```

### Running the Application
1. Ensure the virtual environment is activated.
2. Run the application:
   ```bash
   python run.py
   ```
3. Follow the on-screen prompts:
   - Select the translation direction (English to Spanish or Spanish to English).
   - Enter text to translate or type `exit` to quit.

### Example Usage
```plaintext
┌─ Translator ─┐
│   Welcome to Translator   │
└─ Minimalist & Elegant ─┘
Choose translation direction:
  [1] English to Spanish
  [2] Spanish to English
Enter [1] or [2] [1]: 2

┌──────────────────────────────┐
│ Ready to translate from Spanish to English. Type 'exit' to quit. │
└──────────────────────────────┘
Text to translate (Spanish): hola
Translating...

┌──────────────────────┐
│ Spanish  hola        │
│ English  hello       │
└──────────────────────┘
```

## Project Structure
The project is organized for clarity and scalability:

```
translate_terminal/
├── translator/
│   ├── __init__.py       # Package initialization
│   ├── config.py         # Centralized configuration
│   ├── ui.py             # User interface logic
│   ├── translator.py     # Translation logic
│   ├── validator.py      # Input validation
│   └── main.py           # Application orchestration
└── run.py                # Entry point
```

## Contributing
We welcome contributions to enhance Translator. To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code adheres to the project's style guidelines and includes appropriate tests.

## Support
If you encounter issues or have questions, please open an issue on the project's repository or contact the maintainers.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
*Designed with simplicity and elegance in mind, Translator brings seamless bilingual communication to your terminal.*