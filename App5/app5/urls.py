"""
URL configuration for app5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tripp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name='home'),
    path("dashboard/", views.TripsList, name='trip-list'),
    path("dashboard/note/", views.NoteListView.as_view(), name='note-list'),
    path("dashboard/note/create/", views.NoteCreateView.as_view(), name='note-create'),
    path("dashboard/trip/create", views.TripCreateView.as_view(), name='trip-create'),
    path("dashboard/trip/<int:pk>/", views.TripDetailView.as_view(), name='trip-detail'),
    path("dashboard/trip/<int:pk>/update", views.TripUpdateView.as_view(), name='trip-update'),
    path("dashboard/trip/<int:pk>/delete", views.TripDeleteView.as_view(), name='trip-delete'),
    path("dashboard/note/<int:pk>/", views.NoteDetailView.as_view(), name='note-detail'),
    path("dashboard/note/<int:pk>/update/", views.NoteUpdateView.as_view(), name='note-update'),
    path("dashboard/note/<int:pk>/delete/", views.NoteDeleteView.as_view(), name='note-delete'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/signup/", views.SignupView.as_view(), name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
