# Mini Hospital Management System (HMS)

A Django-based Mini Hospital Management System focused on **doctor availability management**, **patient appointment booking**, and **email notifications using a Serverless service**.

---

##  Project Overview

This project simulates a real-world hospital workflow where:

- **Doctors** manage their availability slots.
- **Patients** view and book available doctor slots.
- **Admin** manages users, roles, slots, and bookings.
- **Email notifications** are sent on signup and booking using a **Serverless (AWS Lambda) service**.

The system ensures **secure authentication**, **role-based access control**, and **transaction-safe booking** to prevent double bookings.

---

##  Features

###  Authentication & Authorization
- Signup and login for Doctor and Patient
- Secure password hashing
- Role-based access control
- Unauthorized access protection

###  Doctor
- Login to doctor dashboard
- Create and manage availability slots
- View booked appointments
- Can only access own data

###  Patient
- Login to patient dashboard
- View all future, unbooked doctor slots
- Book one available slot
- Slot becomes unavailable once booked

###  Admin Panel
- Create and manage users
- Assign roles (doctor / patient)
- Create doctor availability slots
- View all bookings

### Email Notifications (Serverless)
- Separate Serverless email service using Python
- Sends emails for:
  - **Signup Welcome Email**
  - **Booking Confirmation Email**
- Uses SMTP (Mailtrap for local testing)
- Can be tested locally using `serverless-offline`

###  Data Safety
- Database transactions used
- Prevents race conditions using `select_for_update()`
- Ensures no double booking of slots

---

##  Tech Stack

- **Backend:** Django
- **Database:** PostgreSQL / SQLite (local)
- **ORM:** Django ORM
- **Authentication:** Session-based
- **Admin:** Django Admin Panel
- **Email Service:** Serverless Framework (AWS Lambda – local via serverless-offline)

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
