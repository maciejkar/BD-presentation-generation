# BD-presentation-generation

A Python-based desktop application for automated presentation generation built with Kivy framework.

## Project Structure

- `app.py` - Main Kivy application entry point
- `src/` - Source code directory containing core functionality
- `templates/` - Template files for presentations
- `Prezentacje/` - Directory for generated presentations
- `test_code/` - Test files and examples
- `requirements.txt` - Python dependencies
- `settings.json` - Application configuration

## Setup

1. Clone the repository:
```bash
git clone https://github.com/maciejkar/BD-presentation-generation.git
cd BD-presentation-generation
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## Configuration

The application can be configured through `settings.json`. Make sure to review and adjust the settings before running the application.

## Project Features

### Core Components

- Kivy-based desktop GUI application (`app.py`)
- Presentation generation logic in `src/`
- Template system in `templates/`

### Features

- Desktop GUI for presentation management
- Automated presentation generation
- Template-based content creation
- User-friendly interface built with Kivy
- Cross-platform compatibility (Windows, macOS, Linux)

## Development

### Requirements

- Python 3.x
- Kivy
- Other dependencies listed in `requirements.txt`

### System Requirements

- Windows, macOS, or Linux
- Graphics card with OpenGL 2.0 support (for Kivy)

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request

## License

[Add your license information here]