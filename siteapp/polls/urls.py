# from django.urls import path

# from . import views

# urlpatterns = [
    # path("", views.index, name="index"),
    # path("profile", views.profile, name="profile"),
    # path("contact", views.contact, name="contact"),
# ]

from django.urls import path

from . import views

urlpatterns = [
    path("raw", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("contact", views.contact, name="contact"),
    path("", views.html_index, name="html_index"),
    path("address", views.address, name="address"),
    path("phone", views.phone, name="phone"),
]