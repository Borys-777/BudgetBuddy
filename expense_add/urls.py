from. import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name=''),

    path('register', views.register, name='register'),

    path('my-login', views.my_login, name='my-login'),
 ]