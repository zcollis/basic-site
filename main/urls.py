from django.urls import path
from . import views #imports views.py from current directory

urlpatterns = [
path("", views.index, name = "index"),
path("v1/", views.v1, name = "view 1"),
]
