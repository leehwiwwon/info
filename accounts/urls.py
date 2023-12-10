from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('signin/', views.signin, name="signin"),
    path('logingin/', views.logingin, name="loginin"),

]