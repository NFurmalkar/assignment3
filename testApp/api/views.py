import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from rest_framework.response import Response
from testApp.models import Book
from testApp.api.serializers import userSerializer,BookSerializer

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from django import http
from testApp.api.authentication import customAuthentication

from rest_framework.permissions import IsAuthenticated

class register(APIView):
    def post(self,request,*args,**kwargs):
        firstName = request.data.get("firstName")
        lastName = request.data.get("lastName")
        email = request.data.get("email")
        password = request.data.get("password")
        if User.objects.filter(first_name=firstName).exists():
            return Response({'message':"Email Already Exists"},status=status.HTTP_403_FORBIDDEN)
        mydata = {'first_name':firstName,'last_name':lastName,'username':email,'email':email}
        serializer = userSerializer(data=mydata)
        if serializer.is_valid():
            serializer.validated_data['username'] = email
            serializer.validated_data['password'] = make_password(password)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        #print("=========>",serializer.errors)
        return Response(serializer.errors)

class userLogin(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        isValid = auth.authenticate(request,username=email,password=password)
        #print("=======>",isValid,isValid.id)
        if isValid:
            params = {'user':email,'id':isValid.id}
            return Response(params,status=status.HTTP_200_OK)
        else:
            return Response({'message':"Invalid Credentials"},status=status.HTTP_404_NOT_FOUND)

class bookLC(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get_queryset(self):
        qs = Book.objects.all()
        idNo = self.request.GET.get("id")
        print("==========>",idNo)
        if idNo is not None:
            qs = Book.objects.filter(user_id=idNo)
            print("==========>",qs)
            return qs

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        author = request.POST.get("author")
        bookId = request.POST.get("bookId")
        isbn = request.POST.get("isbn")
        userId = request.POST.get("user_id")
        serializer = BookSerializer(data=request.data)
        print(userId)
        if serializer.is_valid():
            userId = User.objects.get(username=userId)
            serializer.validated_data["user_id"] = userId.id
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors)



class bookRUD(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




