from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("contact/add/", views.contact_create, name="contact_add"),
    path("contact/<int:pk>/", views.contact_detail, name="contact_detail"),
    path("contact/<int:pk>/edit/", views.contact_update, name="contact_edit"),
    path("contact/<int:pk>/delete/", views.contact_delete, name="contact_delete"),
]
