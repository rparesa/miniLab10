from booksdir.models import Book, Author, Publisher
from booksdir.serializers import BooksSerializer, AuthorSerializer, PublisherSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def book_list(request, format=None):
	if request.method == 'GET':
		books = Book.objects.all()
		serializer = BooksSerializer(books, many=True)
		return Response(serializer.data)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def book_add(request, format=None):
	if request.method == 'POST':
		serializer = BooksSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def book_details(request, pk, format=None):
	try:
		book = Book.objects.get(pk=pk)
	except Book.DoesNotExits:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = BooksSerializer(book)
		return Reponse(serializer.data)
