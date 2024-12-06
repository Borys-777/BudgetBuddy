from. import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name=''),

    path('register', views.register, name='register'),

    path('my-login', views.my_login, name='my-login'),

    path('user-logout', views.user_logout, name='user-logout'),


    # CRUD functionality 

    path('dashboard', views.dashboard, name='dashboard'),

    path('create-record', views.create_record, name='create-record'),

 ]