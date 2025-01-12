# BD-presentation-generation

A Python-based application for automated presentation generation.

## Project Structure

- `app.py` - Main Flask application entry point
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

## Project Structure

### Core Components

- Flask web application (`app.py`)
- Presentation generation logic in `src/`
- Template system in `templates/`

### Features

- Automated presentation generation
- Template-based content creation
- Web interface for managing presentations

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request

## License

[Add your license information here]