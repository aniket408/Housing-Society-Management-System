from django.contrib import admin
from django.urls import path, re_path
from society import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("logout/", views.logout_view, name="logout"),
    path("action/<str:action_name>/", views.action, name="action"),
    re_path(r"^(?P<page>[A-Za-z0-9_-]+)/?$", views.page, name="page"),
]
