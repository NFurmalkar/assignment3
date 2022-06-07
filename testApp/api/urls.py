from django.contrib import admin
from django.urls import path,include
from testApp.api import views
urlpatterns = [
    path('register-user/',views.register.as_view()),
    path('login-user/',views.userLogin.as_view()),
    #
    path('book-LC/',views.bookLC.as_view()),
    path('book-RUD/<str:pk>/',views.bookRUD.as_view()),
]
