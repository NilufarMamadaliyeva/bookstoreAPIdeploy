from rest_framework import serializers
from books.models import ReviewBookModel, BooksModel,AuthorModel
from users.models import CustomUser

class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel 
        fields = '__all__'

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'

class BookReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    book = serializers.CharField()
    class Meta:
        model = ReviewBookModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    user = serializers.CharField
    class Meta:
        model = CustomUser
        fields = '__all__'