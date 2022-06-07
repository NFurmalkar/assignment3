from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from testApp.models import Book

class userSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'