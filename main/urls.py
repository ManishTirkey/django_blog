
from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path("", views.coverPage, name=("CoverPage")),
    path("blg/", views.Blg, name=("Blg")),
    path("blgposts/<int:slug>/", views.Blgpost, name=("Blgpost")),
]