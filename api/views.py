from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import (
    BookReviewSerializer,
    BooksModelSerializer,
    AuthorModelSerializer,
    UserSerializer,
)
from books.models import ReviewBookModel, BooksModel, AuthorModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from users.models import CustomUser




# Create your views here.


class BooksAPIView(APIView):
    def get(self, request):
        booklist = BooksModel.objects.all()
        serializer = BooksModelSerializer(booklist, many=True)
        # permission_classes = [IsAuthenticated]
        return Response(serializer.data)



class AuthorAPIView(APIView):
    def get(self, request):
        authors = AuthorModel.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(data=serializer.data)

class BookReviewAPIView(APIView):
    def get(self, request):
      books = ReviewBookModel.objects.all()
      paginator = PageNumberPagination()
      page_obj = paginator.paginate_queryset(books, request)
      serializer = BookReviewSerializer(page_obj, many=True)
      return paginator.get_paginated_response(data=serializer.data)

class BookReviewCRUDAPIView(APIView):
    def get(self, request, pk):
        try:
            review = ReviewBookModel.objects.get(id=pk)
        except ReviewBookModel.DoesNotExist:
            return Response(status=404, data={"detail": "Review not found"})

        serializer = BookReviewSerializer(review)
        return Response(data=serializer.data)
        
    def put(self, request, pk):
        try:
            book = ReviewBookModel.objects.get(pk=pk)
        except ReviewBookModel.DoesNotExist:
            return Response(status=404, data={"detail": "Review not found"})
        serializer = BookReviewSerializer(book, data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user']
            book_id = serializer.validated_data['book']
            user = get_object_or_404(CustomUser, pk=user_id)
            book = get_object_or_404(BooksModel, pk=book_id)
            serializer.save(user=user, book=book)
            return Response(serializer.data)
        return Response(serializer.errors, status=400, data={"detail": "Review was not saved"})
    
    def delete(self, request, pk):
        try:
            book = ReviewBookModel.objects.get(pk=pk)
        except ReviewBookModel.DoesNotExist:
            return Response(status=404, data={"detail": "Review not found"})
        book.delete()
        return Response(status=204, data={"detail": "Review may not be exist"})
    




class BooksModelDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            book = BooksModel.objects.get(isbn=pk)
        except BooksModel.DoesNotExist:
            return Response(status=404, data={"detail": "Book not found"})

        serializer = BooksModelSerializer(book)
        return Response(data=serializer.data)

class CustomerAPIView(APIView):
    def get(self, request):
      users = CustomUser.objects.all()
      serializer = UserSerializer(users, many=True)
      return Response(data=serializer.data)
    
