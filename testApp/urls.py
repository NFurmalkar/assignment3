from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login-user/',views.loginUser,name="register"),
    path('logout-user/',views.logoutUser,name="logoutUser"),
    #addBook
    path('add-book/',views.addBook,name="addBook"),
    path('update-book/<int:id>/',views.updateBook,name="updateBook"),
    path('delete-book/<int:id>/',views.deleteBook,name="deleteBook"),

]