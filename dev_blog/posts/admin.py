from django.contrib import admin
from posts.models import Post
from django.utils.html import format_html

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    #list_display = ('title', 'content','image','user', 'category','state', 'created_at', 'updated_at')
    list_display = ('title', 'content','display_image','user', 'category','state', 'created_at', 'updated_at')

    # mostrar imagenes en el panel de administración
    def display_image(self, obj):
      print(obj.image.url)  # Imprime la URL de la imagen para depurar
      return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url) if obj.image else '')
