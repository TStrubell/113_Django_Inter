from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# SELECT * FROM table
# DELETE FROM table WHERE id = ?
# UPDATE (name, lastname) VALUES (?, ?) WHERE id = ?
# CREATE TABLE (
#   id INTEGER PRIMARY_KEY AUTOINCREMENT,
#   name VARCHAR(100),
#   ...
#)
class Post(models.Model):
  title = models.CharField(max_length=128)
  subtitle = models.CharField(max_length=128)
  body = models.TextField()
  create_on = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(
    User, # What model is related to
    on_delete=models.CASCADE  # The action IF a user gets deleted

  )

  def __str__(self):
    return f"{self.title} by {self.author}"

  def get_absolute_url(self):
    # Automatically redirects the user to a specific endpoint when a success POST request is made
    return reverse("post_detail", args=[self.id])

  
