from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from . models import Book
import requests

# Create your views here.

def register(request):
    if request.method == "POST":
        fname = request.POST.get("fName")
        lname = request.POST.get("LName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mydata = {'firstName':fname,'lastName':lname,'email':email,'password':password}
        #call API Urls
        api_url = "http://127.0.0.1:8000/api/register-user/"
        response = requests.post(api_url,data=mydata)
        print(response,mydata,response.json())
        if response.status_code == 201:
            messages.success(request, "Register Successfully")
            return redirect('/')
        else:
            resData = response.json()
            messages.success(request,resData.get('message'))
            redirect('/register')

    return render(request,'libApp/register.html')

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        mydata = {'email':email,'password':password}
        api_url = "http://127.0.0.1:8000/api/login-user/"
        response = requests.post(api_url, data=mydata)
        print("response======>",response.json())
        if response.status_code == 200:
            resData = response.json()
            request.session['userEmail'] = resData.get('user')
            request.session['userId'] = resData.get('id')
            #messages.success(request, "Register Successfully")
            return redirect('/')
        else:
            resData = response.json()
            messages.success(request, resData.get('message'))
            redirect('/register')

    return render(request,'libApp/login.html')

def logoutUser(request):
    del request.session['userEmail']
    del request.session['userId']
    return redirect('/login-user')

def home(request):
    userId = request.session.get('userEmail')
    tokenId = request.session.get('userId')
    if userId == None:
        return redirect('/login-user')
    api_url = "http://127.0.0.1:8000/api/book-LC/?id="+str(tokenId)
    response = requests.get(api_url)
    print(response.json())
    #print("===>",request.session.get('userEmail'))
    #print("===>",request.session.get('userId'))
    params = {'bookData':response.json()}
    return render(request,'libApp/home.html',params)

def addBook(request):
    if request.method == "POST":
        userId = request.session.get('userEmail')
        if userId == None:
            return redirect('/login-user')
        name = request.POST.get("name")
        author = request.POST.get("author")
        bookId = request.POST.get("bookId")
        isbn = request.POST.get("isbn")

        mydata = {'name':name,'author':author,'bookId':bookId,'isbn':isbn,'user_id':userId}
        api_url = "http://127.0.0.1:8000/api/book-LC/"
        response = requests.post(api_url, data=mydata)
        print(response, mydata)
        return redirect('/')

def updateBook(request,id):
    book = Book.objects.get(id=id)
    userId = request.session.get('userEmail')
    if userId == None:
        return redirect('/login-user')
    name = request.POST.get("name")
    author = request.POST.get("author")
    bookId = request.POST.get("bookId")
    isbn = request.POST.get("isbn")
    mydata = {'name': name, 'author': author, 'bookId': bookId, 'isbn': isbn}
    #call Url
    api_url = "http://127.0.0.1:8000/api/book-RUD/"+str(id) +'/'
    response = requests.put(api_url, data=mydata,)
    print(response.json())
    return redirect('/')
    #return render(request,'libApp/home.html')

def deleteBook(request,id):
    userId = request.session.get('userEmail')
    if userId == None:
        return redirect('/login-user')
    # call Url
    api_url = "http://127.0.0.1:8000/api/book-RUD/" + str(id) + '/'
    response = requests.delete(api_url)
    return redirect('/')


