from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category
from slugify import slugify
from .logic.image import generate_unique_filename
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #slug = models.SlugField(max_length=255, unique=True)
    # auto generar el slug
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    #image = models.ImageField(upload_to='uploads/posts')
    # agregar un nombre unico al archivo
    image = models.ImageField(upload_to=generate_unique_filename)
    # auto generar la fecha, en base a la fecha del servidor
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=None, blank=True, null=True)
    # Para eliminar el post de lista de posts, pero no de la base de datos
    state = models.BooleanField(default=True) 
    # cuando se elimina el usuario, sus posts se eliminan
    #user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    # cuando se elimina el usuario, el post queda en null
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    
    # para que se muestre el título en el panel de administración
    def __str__(self):
      return self.title

    #garantiar que el slug sea unico, son metodos propios de django
    def save(self, *args, **kwargs):
      if not self.slug:
          base_slug = slugify(self.title)
          self.slug = self.get_unique_slug(base_slug)
      # Actualiza la fecha cada vez que se guarda
      self.updated_at = datetime.now()  
      super().save(*args, **kwargs)
  
    def get_unique_slug(self, base_slug):
      slug = base_slug
      counter = 1
      while Post.objects.filter(slug=slug).exists():
          slug = f"{base_slug}-{counter}"
          counter += 1
      return slug