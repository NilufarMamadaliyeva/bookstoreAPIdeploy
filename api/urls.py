from django.urls import path
from .views import BookReviewAPIView,AuthorAPIView,BooksAPIView,BookReviewCRUDAPIView,BooksModelDetailAPIView, CustomerAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'
urlpatterns = [
    path('reviews/',BookReviewAPIView.as_view(), name='reviews-api'),
    path('books/',BooksAPIView.as_view(), name='books-api'),
    path('author/',AuthorAPIView.as_view(),name='authors-api'),
    path('review/<int:pk>/',BookReviewCRUDAPIView.as_view(), name='review-api'),
    path('book/<int:pk>/',BooksModelDetailAPIView.as_view(),name='book-api'),
    path('users/',CustomerAPIView.as_view(),name='users-api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
