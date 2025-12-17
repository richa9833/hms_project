from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import transaction
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Availability, Booking
from users.models import User


@login_required
def dashboard_redirect(request):
    """Redirect logged-in user to their correct dashboard based on role"""
    if request.user.role == "patient":
        return redirect("patient_dashboard")
    elif request.user.role == "doctor":
        return redirect("doctor_dashboard")
    else:
        return HttpResponse("Invalid role")


@login_required
def patient_dashboard(request):
    today = timezone.now().date()
    slots = Availability.objects.filter(
        date__gte=today,
        is_booked=False
    ).select_related('doctor')

    return render(request, "patient_dashboard.html", {
        "slots": slots
    })


@login_required
def book_slot(request, slot_id):
    slot = get_object_or_404(
        Availability.objects.select_for_update(),
        id=slot_id
    )

    if slot.is_booked:
        return HttpResponse("Slot already booked")

    with transaction.atomic():
        slot.is_booked = True
        slot.save()

        Booking.objects.create(
            doctor=slot.doctor,
            patient=request.user,
            availability=slot
        )

    return redirect("patient_dashboard")


@login_required
def doctor_dashboard(request):
    slots = Availability.objects.filter(doctor=request.user)
    return render(request, "doctor_dashboard.html", {
        "slots": slots
    })
