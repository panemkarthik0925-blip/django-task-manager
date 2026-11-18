
# Django Task Manager

A full-stack task management web application built with Python and Django. Users can create accounts, manage their personal tasks, track progress, and organize their work through search and filtering.

## Features

- User registration, login, and logout
- Create, view, edit, and delete tasks (CRUD)
- Mark tasks as completed or pending
- User-specific task management
- Search tasks by title
- Filter tasks by completion status
- Dashboard statistics for total, completed, and pending tasks
- Pagination for task lists
- Responsive interface with HTML and CSS
- SQLite database

## Tech Stack

- Backend: Python, Django
- Frontend: HTML, CSS, Django Templates
- Database: SQLite
- Version Control: Git and GitHub

## Project Structure

    django_task_manager/
    ├── config/
    │   ├── settings.py
    │   └── urls.py
    ├── tasks/
    │   ├── migrations/
    │   ├── templates/
    │   │   └── tasks/
    │   ├── models.py
    │   ├── views.py
    │   ├── forms.py
    │   └── urls.py
    ├── manage.py
    ├── requirements.txt
    └── README.md

## Installation

### 1. Clone the repository

    git clone https://github.com/YOUR_USERNAME/django-task-manager.git
    cd django-task-manager

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

Windows PowerShell:

    python -m venv venv
    .\venv\Scripts\Activate.ps1

### 3. Install dependencies

    python -m pip install -r requirements.txt

### 4. Apply database migrations

    python manage.py migrate

### 5. Create an administrator (optional)

    python manage.py createsuperuser

### 6. Start the development server

    python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

## Usage

1. Register a new account.
2. Log in to access your dashboard.
3. Create and manage your tasks.
4. Search by task title or filter by status.
5. Track your progress using dashboard statistics.

## Future Improvements

- Add task due dates and priorities
- Add automated tests
- Improve the user interface
- Add PostgreSQL support
- Deploy the application online

## Author

YOUR NAME

## License

This project is available for educational and portfolio purposes.
