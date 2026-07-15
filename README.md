# 🌦️ Weather Dashboard using Django

A fundamental Django project built as part of my Django learning journey. This project integrates a live Weather API, stores weather data in a MySQL database using Django ORM, and includes a basic user registration and login system.

---

## 🚀 Features

- User Registration
- User Login
- Live Weather API Integration
- Display Current Weather Details
- Store Weather Data in MySQL
- Django ORM
- Django Admin Panel
- MySQL Database Connectivity

---

## 🛠️ Technologies Used

- Python
- Django
- MySQL
- HTML
- WeatherAPI
- Django ORM

---

## 📂 Project Structure

```
weather_project/
│
├── weather/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│
├── templates/
│   ├── register.html
│   ├── login.html
│   └── home.html
│
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Nikhildusa07/weather-dashboard.git

cd weather-dashboard
```

### Install Dependencies

```bash
pip install django

pip install requests

pip install mysqlclient
```

### Configure MySQL

Create a database named:

```text
weather_dashboard
```

Update the `DATABASES` configuration in `settings.py`.

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📌 Project Workflow

```
User
   │
   ▼
Registration
   │
   ▼
Login
   │
   ▼
Weather Dashboard
   │
   ▼
Weather API
   │
   ▼
JSON Response
   │
   ▼
Django ORM
   │
   ▼
MySQL Database
   │
   ▼
Display Weather Data
```

---

## 📖 Concepts Practiced

- Django Project & App
- URL Routing
- Function-Based Views
- Templates
- Forms
- POST Requests
- Django Models
- Django ORM
- MySQL Integration
- Weather API Integration
- User Registration & Login
- Django Admin

---

## 🔮 Future Improvements

- Django Authentication
- Sessions
- Logout
- Template Inheritance
- Static Files
- Bootstrap UI
- Search Weather by City
- Weather History
- Deployment

---

## 👨‍💻 Author

**Nikhil Dusa**

GitHub: https://github.com/Nikhildusa07

---

⭐ This project was developed as part of my Django learning journey to strengthen my backend development skills and understand real-world Django concepts.
