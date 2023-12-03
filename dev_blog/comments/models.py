from django.db import models
from django.db.models import CASCADE
from datetime import datetime

class Comment(models.Model):
  post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True)
  user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
  content = models.TextField(max_length=255)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  updated_at = models.DateTimeField(default=None, blank=True, null=True)
  state = models.BooleanField(default=True)
  
  #garantiar que el slug sea unico, son metodos propios de django
  def save(self, *args, **kwargs):
    self.updated_at = datetime.now()  
    super().save(*args, **kwargs)
  
  
  def __str__(self):
    return f"{self.user.username}-{self.created_at.strftime('%Y-%m-%d-%H:%M:%S')}"