# Django Todo App

A feature-rich task management application built with Django that helps you organize and track your daily tasks efficiently.

![Django Version](https://img.shields.io/badge/django-5.2.5-green.svg)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)

<img width="1919" height="969" alt="Image" src="https://github.com/user-attachments/assets/8e812c46-4165-4d1f-b655-b06bda117d71" />

<img width="1919" height="972" alt="Image" src="https://github.com/user-attachments/assets/04f25d35-2620-4b62-9d06-bfff320ae77b" />

## Features

- ✨ Create, Read, Update, and Delete tasks (CRUD operations)
- ✅ Mark tasks as completed/uncompleted
- 📱 Responsive design using Bootstrap
- 🎯 Simple and intuitive user interface
- 📋 Separate views for active and completed tasks
- 🔄 Real-time updates without page refresh

## Technologies Used

- **Backend Framework:** Django
- **Frontend:** HTML, CSS, Bootstrap 5
- **Icons:** Font Awesome
- **Database:** SQLite (default Django database)

## Setup Instructions

1. Clone the repository

```bash
git clone <your-repository-url>
cd TODO_APP
```

2. Create a virtual environment and activate it

```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python -m venv env
source env/bin/activate
```

3. Install required packages

```bash
pip install django
```

4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server

```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000` in your browser

## Project Structure

```
TODO_APP/
│
├── ToDo/                   # Main application directory
│   ├── migrations/         # Database migrations
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   └── urls.py            # URL patterns
│
├── templates/             # HTML templates
│   ├── home.html         # Main task list view
│   └── edit_task.html    # Task editing view
│
├── todo_main/            # Project settings directory
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
│
├── manage.py             # Django management script
└── README.md            # Project documentation
```

## Features in Detail

### Task Management

- **Add Task:** Simple input form at the bottom of the page
- **Edit Task:** Click the pencil icon to modify existing tasks
- **Delete Task:** Remove tasks using the trash icon
- **Mark Complete/Incomplete:** Toggle task status with checkmark/cross icons

### User Interface

- Clean and intuitive design
- Responsive layout that works on all devices
- Clear visual indicators for task status
- Easy-to-use action buttons for each task

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- Bootstrap for the responsive design
- Font Awesome for the beautiful icons
- Django documentation for the excellent resources
