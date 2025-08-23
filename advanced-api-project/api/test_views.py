# api/test_views.py

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book

class BookAPITests(APITestCase):
    """
    This class contains unit tests for the Book API endpoints.
    It covers CRUD operations, permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        """
        Set up the necessary objects for testing. This method runs before every test.
        """
        # Create a test user for authenticated requests.
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Log the test client in with the created user.
        # This will attach an authentication token to all subsequent requests from this client.
        self.client.login(username='testuser', password='password123')
        
        # Creates a test client that is not authenticated for permission tests.
        self.unauthenticated_client = self.client.__class__()
        
        # Creates multiple Book instances to test list, filtering, and ordering.
        self.book1 = Book.objects.create(
            title='The Hitchhiker\'s Guide to the Galaxy',
            author='Douglas Adams',
            publication_date='1979-10-12',
            isbn='9780345391803'
        )
        self.book2 = Book.objects.create(
            title='The Lord of the Rings',
            author='J.R.R. Tolkien',
            publication_date='1954-07-29',
            isbn='9780618053267'
        )
        self.book3 = Book.objects.create(
            title='Dune',
            author='Frank Herbert',
            publication_date='1965-08-01',
            isbn='9780441172719'
        )
        self.book4 = Book.objects.create(
            title='The Good Doctor',
            author='Joshua Odedeyi',
            publication_date='19-08-01',
            isbn='9780441172719'
        )

    # --- Test Cases for CRUD Operations (Authenticated) ---

    def test_book_list_authenticated(self):
        """
        Ensure the authenticated user can retrieve a list of books.
        """
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the number of books in the response matches the number created.
        self.assertEqual(len(response.data), 3)

    def test_create_book(self):
        """
        Ensure an authenticated user can create a new book.
        """
        url = reverse('book-create')
        data = {
            'title': 'The Catcher in the Rye',
            'author': 'J.D. Salinger',
            'publication_date': '1951-07-16',
            'isbn': '9780316769488'
        }
        response = self.client.post(url, data, format='json')
        # Assert that the status code is 201 Created.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that the number of books in the database has increased by one.
        self.assertEqual(Book.objects.count(), 4)
        # Assert that the created book's title is correct.
        self.assertEqual(Book.objects.get(title='The Catcher in the Rye').author, 'J.D. Salinger')

    def test_retrieve_book(self):
        """
        Ensure an authenticated user can retrieve a single book by ID.
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the retrieved book's title matches the one we created.
        self.assertEqual(response.data['title'], self.book1.title)
    
    def test_update_book(self):
        """
        Ensure an authenticated user can update a book.
        """
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        # Use PATCH for a partial update.
        updated_data = {'title': 'The Hitchhiker\'s Guide to the Galaxy (Revised)'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Refresh the book instance from the database and check the updated title.
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, updated_data['title'])

    def test_delete_book(self):
        """
        Ensure an authenticated user can delete a book.
        """
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        # Assert that the status code is 204 No Content.
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Assert that the book has been removed from the database.
        self.assertEqual(Book.objects.count(), 2)
        # Check that the deleted book no longer exists.
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=self.book1.pk)

    # --- Test Cases for Permissions (Unauthenticated) ---

    def test_unauthenticated_book_list(self):
        """
        Ensure unauthenticated users can view the list of books (read-only).
        """
        url = reverse('book-list')
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_create_book_fails(self):
        """
        Ensure unauthenticated users cannot create a book.
        """
        url = reverse('book-create')
        data = {'title': 'Forbidden Book'}
        response = self.unauthenticated_client.post(url, data, format='json')
        # Assert that the request is forbidden.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_unauthenticated_retrieve_book(self):
        """
        Ensure unauthenticated users can retrieve a single book (read-only).
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_update_book_fails(self):
        """
        Ensure unauthenticated users cannot update a book.
        """
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        updated_data = {'title': 'Forbidden Update'}
        response = self.unauthenticated_client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_delete_book_fails(self):
        """
        Ensure unauthenticated users cannot delete a book.
        """
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- Test Cases for Filtering, Searching, and Ordering ---

    def test_filter_by_title(self):
        """
        Ensure the API can filter books by title.
        """
        # The filterset_fields = ['title', 'author__name', 'publication_year'] will be used here.
        url = reverse('book-list') + '?title=Dune'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')
    
    def test_search_by_title(self):
        """
        Ensure the API can search for books by title.
        """
        # The search_fields = ['title', 'author__name'] will be used here.
        url = reverse('book-list') + '?search=hitchhiker'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hitchhiker\'s Guide to the Galaxy')

    def test_ordering_by_title(self):
        """
        Ensure the API can order books by title.
        """
        # The ordering_fields = ['title', 'publication_year'] will be used here.
        url = reverse('book-list') + '?ordering=-title'  # Descending order by title
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the first book in the list is 'The Lord of the Rings' (alphabetically last).
        self.assertEqual(response.data[0]['title'], 'The Lord of the Rings')

