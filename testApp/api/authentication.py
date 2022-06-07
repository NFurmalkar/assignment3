from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from testApp.models import Book
from django.shortcuts import redirect

class customAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get("token")
        print("token",token)
        if token is None or token =="":
            return None
        customer = None
        try:
            user = User.objects.get(username=token)
        except:
            raise AuthenticationFailed("Credentials are not valid")
        return (user,None)