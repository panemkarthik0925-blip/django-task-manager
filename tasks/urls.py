
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/<int:task_id>/edit/", views.edit_task, name="edit_task"),
    path("tasks/<int:task_id>/toggle/", views.toggle_task, name="toggle_task"),
    path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
