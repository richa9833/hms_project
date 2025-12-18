# Mini Hospital Management System (HMS)

A Django-based Mini Hospital Management System focused on **doctor availability management** and **patient appointment booking** with **role-based authentication**.

---

## Project Overview

This project simulates a real-world hospital workflow where:

- **Doctors** can manage their availability slots.
- **Patients** can view and book available doctor slots.
- **Admin** can manage users, roles, slots, and bookings.

The system ensures **secure authentication**, **role-based access control**, and **transaction-safe booking** to avoid double bookings.

---

##  Features

###  Authentication & Authorization
- Signup and login for Doctor and Patient
- Secure password hashing
- Role-based access control
- Unauthorized access protection

###  Doctor
- Login to doctor dashboard
- View own availability slots
- View booked appointments
- Cannot access patient features

###  Patient
- Login to patient dashboard
- View all future, unbooked doctor slots
- Book one available slot
- Once booked, slot becomes unavailable to others

###  Admin Panel
- Create and manage users
- Assign roles (doctor/patient)
- Create doctor availability slots
- View all bookings

###  Data Safety
- Uses database transactions
- Prevents race conditions using `select_for_update()`
- Ensures no double booking of slots

---

##  Tech Stack

- **Backend:** Django
- **Database:** PostgreSQL
- **ORM:** Django ORM
- **Authentication:** Session-based
- **Admin:** Django Admin Panel

---

##  Project Structure

    hms_project/
    │
    ├── hms/                    # Project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── users/                  # Authentication & roles
    │   ├── models.py           # Custom User (doctor / patient)
    │   ├── views.py            # Signup & login
    │   ├── urls.py
    │
    ├── appointments/           # Core hospital logic
    │   ├── models.py           # Availability & Booking
    │   ├── views.py            # Dashboards & booking
    │   ├── urls.py
    │
    ├── templates/              # HTML templates
    │   ├── login.html
    │   ├── signup.html
    │   ├── patient_dashboard.html
    │   └── doctor_dashboard.html
    ├── email_services/
    │   ├── handler.py
    │   ├── serverless.yml
    │   ├── requirements.txt
    ├── manage.py
    ├── db.sqlite3              # Database
    └── README.md
