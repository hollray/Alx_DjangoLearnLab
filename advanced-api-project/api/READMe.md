# API Documentation for advanced_api_project

## Book Endpoints

The Book API provides endpoints to manage book records.

### Endpoints

-   **`GET /api/books/`**
    -   **Description:** Retrieves a list of all books.
    -   **Permissions:** Read-only access is allowed for unauthenticated users.
    -   **Example Response (200 OK):**
        ```json
        [
          {
            "id": 1,
            "title": "The Good Doctor by Ray",
            "author": "Joshua Odedeyi",
            "publication_date": "1968-10-12",
            "isbn": "9780345391803"
          }
        ]
        ```

-   **`POST /api/books/`**
    -   **Description:** Creates a new book record.
    -   **Permissions:** Requires an authenticated user.
    -   **Request Body:** JSON object with `title`, `author`, `publication_date`, and `isbn`.
    -   **Example Response (201 Created):**
        ```json
        {
          "id": 2,
          "title": "New Book Title",
          "author": "Author Name",
          "publication_date": "2023-01-01",
          "isbn": "9781234567890"
        }
        ```

-   **`GET /api/books/<int:pk>/`**
    -   **Description:** Retrieves a single book by its ID.
    -   **Permissions:** Requires an authenticated user.

-   **`PUT/PATCH /api/books/<int:pk>/`**
    -   **Description:** Updates an existing book.
    -   **Permissions:** Requires an authenticated user.

-   **`DELETE /api/books/<int:pk>/`**
    -   **Description:** Deletes an existing book.
    -   **Permissions:** Requires an authenticated user.