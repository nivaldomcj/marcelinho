# Marcelinho Bot

A Django-based bot application.

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd marcelinho
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Copy `.env.example` to `.env` and update the values:
   ```bash
   cp .env.example .env
   ```

5. **Set up PostgreSQL**
   - Create a new PostgreSQL database named `marcelinho_db`
   - Update the database credentials in `.env`

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Project Structure

- `config/` - Main project configuration
- `bot/` - Bot application
- `.env` - Environment variables (not versioned)
- `requirements.txt` - Python dependencies

## Development

- Python 3.8+
- Django 5.2.5
- PostgreSQL
