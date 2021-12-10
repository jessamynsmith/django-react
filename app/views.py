import requests

from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication


class HomeView(TemplateView):
    template_name = 'app/home.html'


class BooksView(APIView):
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, format=None):
        """
        Return a list of all books.
        """
        response = requests.get("https://www.anapioficeandfire.com/api/books")
        books = []
        if response.status_code == 200:
            books = response.json()

        return Response(books)
