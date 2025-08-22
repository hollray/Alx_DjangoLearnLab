""" This serializer is for Author and Books models
it contains thee following:
- a customized validationdefinition
- a demonstrated nesting of related books dynamically"""

from rest_framework import serializers
from .models import Author, Book
from datetime import datetime 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

        #customized validation definition
    
    def validate_publication_year(self, valueofyear):
        current_year = datetime.now().year
        if valueofyear > current_year:
            raise serializers.ValidationError("Apologies, Year of publication cannot be greater than present year")
        return valueofyear
    


class AuthorSerializer(serializers.ModelSerializer):
    # this section demonstrates nesting related books dynamically
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']