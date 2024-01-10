# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    
    # User management - Django's built-in views (e.g., login, logout)
    path("accounts/", include("django.contrib.auth.urls")),
    
    # User management - Custom views (e.g., signup)
    path("accounts/", include("accounts.urls")),  # new

    # Local apps
    path("", include("pages.urls")),
]
