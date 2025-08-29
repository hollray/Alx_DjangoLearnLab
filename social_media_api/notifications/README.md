Like a Post: Send a POST request to http://127.0.0.1:8000/api/posts/<post_id>/like/. The first time you do this, a like is created. The second time, the like is deleted (unliking the post).

View Notifications: Send a GET request to http://127.0.0.1:8000/api/notifications/ with a user's authentication token. You will see a list of notifications for that user.