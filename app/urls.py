from django.urls import path

from app import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('api/v1/books/', views.BooksView.as_view(), name='books_list'),
]
