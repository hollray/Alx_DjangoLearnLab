from rest_framework import serializers
from .models import Book


# Defined Serializer
class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book
        fields = '__all__'  # This includes all fields of the Book model
        # fields = ['id', 'title','author']