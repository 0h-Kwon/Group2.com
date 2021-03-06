from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("", views.main, name="main"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("notice",views.notice_view, name="notice"),
    path('<int:id>/det/', views.notDet_view, name='notDet'),
    path("manage", views.manage_view, name="manage"),
    path("intro", views.intro_view, name="intro"),
    path('<int:id>/info/', views.info_view, name="info"),
    path("modinfo", views.modinfo_view, name="modinfo"),
]
