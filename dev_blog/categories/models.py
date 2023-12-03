from django.db import models
from datetime import datetime

class Category(models.Model):
  title= models.CharField(max_length=50)
  description = models.TextField(max_length=255)
  # se utiliza para crear urls amigables
  slug = models.SlugField(max_length=50, unique=True)
  published = models.BooleanField(default=False)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  
  
  # para que se muestre el título en el panel de administración
  def __str__(self):
    return self.title
  
  
  


