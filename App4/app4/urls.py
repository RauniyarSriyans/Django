"""
URL configuration for app4 project.

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
from django.contrib import admin
from django.urls import path
from linktree.views import LinkListView, LinkCreateView, LinkUpdateView, LinkDeleteView, ProfileView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LinkListView.as_view(), name="link-list"),
    path("create/", LinkCreateView.as_view(), name="link-create"),
    path("update/<int:pk>/", LinkUpdateView.as_view(), name="link-update"),
    path("delete/<int:pk>/", LinkDeleteView.as_view(), name="link-delete"),
    path("<slug:profile_slug>/", ProfileView, name="profile"),
]
