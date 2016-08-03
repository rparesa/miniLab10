from rest_framework import serializers 
from booksdir.models import Book, Author, Publisher

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('fname','lname')
class PublisherSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Publisher
		fields = ('__all__')

class BooksSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(read_only=True,many=True)
	publisher = PublisherSerializer(read_only=True,many=True)     
	class Meta:         
		model = Book         
		fields = ('title','author', 'pub_date', 'summary', 'price', 'link', 'img', 'publisher')

