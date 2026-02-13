
from django.db import models
from django.contrib.auth.models import User as UserModel

# deprecated User model, using Django's built-in User model instead
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)  # User's unique username
    email = models.EmailField(unique=True)  # User's unique email
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the user was created


    def __str__(self):
        return self.username


# Post model with different types and metadata
class Post(models.Model):
    POST_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    metadata = models.JSONField(default=dict, blank=True)

    author = models.ForeignKey(
        UserModel,
        related_name='posts',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"


# Comment model
class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(UserModel, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"


# Like model
class Like(models.Model):
    author = models.ForeignKey(UserModel, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Like by {self.author.username} on Post {self.post.id}"

