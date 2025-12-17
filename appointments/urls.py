from django.urls import path
from .views import patient_dashboard, doctor_dashboard, book_slot, dashboard_redirect

urlpatterns = [
    # Root → redirect based on user role
    path("", dashboard_redirect, name="dashboard_redirect"),

    # Patient dashboard & booking
    path("patient/dashboard/", patient_dashboard, name="patient_dashboard"),
    path("patient/book/<int:slot_id>/", book_slot, name="book_slot"),

    # Doctor dashboard
    path("doctor/dashboard/", doctor_dashboard, name="doctor_dashboard"),
]
