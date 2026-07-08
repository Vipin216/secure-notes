# 🔒 Secure Notes Platform

A secure note management web application built with **Django**, **Django REST Framework**, **PostgreSQL**, and **AWS**, focusing on secure authentication, encrypted data storage, REST APIs, and cloud deployment.

---

## ✨ Features

### Authentication & Authorization

* User authentication with Django sessions
* JWT authentication for REST APIs
* Google OAuth 2.0 login using **django-allauth**
* Ownership-based authorization to ensure users can only access their own notes

### Secure Notes

* Create, view, edit, and delete notes
* **Fernet-based encryption** for note contents before storing them in the database
* Automatic decryption when notes are displayed to authorized users
* Note titles remain plaintext to support searching

### REST APIs

* CRUD APIs built using Django REST Framework
* JWT-protected API endpoints
* User registration API
* Pagination
* Search (by title)
* API throttling (100 requests/minute per user)

### Audit Logging

Automatically records note-related actions:

* Note Created
* Note Edited
* Note Deleted

### Database

* PostgreSQL database
* User–Note relationship using Django ORM
* Audit log model for tracking note activity

### Deployment

* Deployed on **AWS EC2**
* PostgreSQL hosted on **Amazon RDS**
* Environment variables used for sensitive configuration
* WhiteNoise configured for static file serving

---

# 🏗️ Tech Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* PostgreSQL

### Authentication

* Django Authentication
* JWT (SimpleJWT)
* Google OAuth (django-allauth)

### Security

* Fernet Symmetric Encryption
* Ownership-based Authorization
* Environment Variables (.env)

### Cloud

* AWS EC2
* AWS RDS

### Other

* Git
* GitHub
* WhiteNoise

---

# 🔐 Security Features

* Session-based authentication for the web application
* JWT authentication for REST APIs
* Google OAuth login
* User-level authorization
* API throttling
* Environment variables for secrets management
* **Encryption at Rest** using Fernet

All note contents are encrypted before being stored in PostgreSQL and decrypted only when accessed by an authenticated and authorized user.

---

# 📊 Project Highlights

* ✅ Implemented **10+ backend features**
* 🔒 **100% of note contents encrypted at rest**
* ☁️ Deployed using **AWS EC2 + Amazon RDS PostgreSQL**
* 🔑 Supports both Session Authentication and JWT Authentication
* 🌐 Integrated Google OAuth 2.0 login
* 📜 Built-in audit logging for note modifications

---

# 📂 Project Structure

```text
securenote/
│
├── notes/
│   ├── api/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── utils.py
│   └── urls.py
│
├── securenote/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── requirements.txt
├── manage.py
└── .env
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/Secure-Notes.git
cd Secure-Notes
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

ENCRYPTION_KEY=your_fernet_key
```

---

# 🗄️ Database Setup

Run migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the server:

```bash
python manage.py runserver
```

---

# 📸 Screenshots

You can add screenshots here later:

* Login Page
* Google OAuth Login
* Notes Dashboard
* Create Note
* Encrypted Database Entry
* AWS Deployment

---

# 🚀 Future Improvements

* Login and Logout audit logging
* Gunicorn production server
* Nginx reverse proxy
* HTTPS
* Application Load Balancer (ALB)
* Auto Scaling Group (ASG)
* CloudWatch monitoring

---

# 📚 Learning Outcomes

This project provided hands-on experience with:

* Django application development
* REST API development using DRF
* JWT authentication
* OAuth 2.0 integration
* PostgreSQL database management
* Encryption at rest using Fernet
* AWS EC2 deployment
* Amazon RDS
* Secure configuration management using environment variables
* Backend security best practices

---

# 👨‍💻 Author

**Vipin**

Built as a backend-focused portfolio project to strengthen skills in Django, cloud deployment, and application security.
