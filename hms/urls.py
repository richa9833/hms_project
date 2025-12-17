from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # App URLs
    path('', include('appointments.urls')),

    # Users URLs for signup/login
    path('', include('users.urls')),  # include at root
]
