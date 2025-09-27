from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # ListAPIView
    path('', include(router.urls)),  # ViewSet CRUD routes
]

urlpatterns += [
    path('get-token/', obtain_auth_token, name='get-token'),
]
