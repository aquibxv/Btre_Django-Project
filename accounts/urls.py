from django.urls import path
from . import views

# listings/
urlpatterns = [
   path('login', views.login, name="login"),
   path('register', views.register, name="register"),
   path('logout', views.logout, name="logout"),
   path('dashbaord', views.dashboard, name="dashboard"),
]