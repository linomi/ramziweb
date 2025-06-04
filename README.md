# Django Blog and Scholar Website

A Django-based web application that combines a blog system with a scholar prompt feature.

## Features

### Blog Application
- Full-featured blog system
- Post management with slugs and excerpts
- Author management
- Tag and category system for posts
- Comment functionality
- Custom template system

### Scholar Prompt Application
- PDF processing capabilities
- Interactive playground (Jupyter notebook integration)
- Custom forms for scholar interactions

## Requirements

- Python 3.11+
- Django
- Other dependencies (install via requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ramziweb
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Project Structure

- `blog/` - Main blog application
  - Models for posts, authors, tags, categories, and comments
  - Custom templates and static files
  - URL routing and views

- `scholar_prompt/` - Scholar application
  - PDF processing functionality
  - Interactive playground
  - Custom forms and views

- `static/` - Global static files
  - CSS stylesheets
  - JavaScript files

- `templates/` - Global templates
  - Base template layout
  - Error pages

## Configuration

The main project settings are in `ramziweb/settings.py`. Key configurations:
- Database settings
- Static and media files configuration
- Installed applications
- Middleware setup

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


