from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response
# manejo de archivos
from django.core.files.storage import default_storage
from django.core.files import File
import os
# permisos
from posts.api.permissions import IsAdminOrReadOnly
# filtros
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    #queryset = Post.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    # agregar libreria de filtrado
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'user']
    # filtrado por un atributo de un modelo relacionado
    #filterset_fields = ['category__slug', 'user__username']

    # sobreescribir metodo get_queryset, en cada peticion se ejecuta
    def get_queryset(self):
      user = self.request.user
      # si es super usuario, se listan todas las categorias
      if user.is_superuser:
          return Post.objects.all()
      # si no es super usuario, se listan solo las categorias publicadas
      else:
          return Post.objects.filter(state=True)
          
    #definir respuestas a los metodos http
    def create(self, request,*args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Post created successfully'}, status=status.HTTP_201_CREATED)
      return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,*args, **kwargs):
      # siempre se debe valdar una respuesta con detail, si no envia id
      try:
        # manejo de imagen
        instance = self.get_object()
        data_imagen = request.data.get('image')
        
        # Crear una copia mutable de request.data
        mutable_data = request.data.copy()
        
        # Obtener la ruta de la imagen actual
        ruta_imagen_actual = instance.image.path if instance.image else None

        # Si 'image' es una URL, no actualices el campo
        if isinstance(data_imagen, str) and 'http' in data_imagen:
          mutable_data.pop('image', None)
        else:
          # Si 'image' es un archivo, actualiza el campo
          mutable_data['image'] = data_imagen

        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        serializer = self.get_serializer(instance, data=mutable_data, partial=True)

        if serializer.is_valid():
          serializer.save()
          
          # Confirmar que la actualización fue exitosa
          instance.refresh_from_db()
          
          # Eliminar la imagen anterior
          if ruta_imagen_actual and os.path.isfile(ruta_imagen_actual):
            default_storage.delete(ruta_imagen_actual)
                
          return Response({'message': 'Post updated successfully'})
      except Exception  as e:
        return Response({'error': f'Cannot update Post. {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
      
    def destroy(self, request, *args, **kwargs ):
      # siempre se debe valdar una respuesta con detail, si no envia id
      try:
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Post deleted successfully'}, status=status.HTTP_200_OK)
      except Exception  as e:
        return Response({'error': f'Cannot delete Post. {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
          
    def list(self, request,*args, **kwargs):
      try:
        #queryset = Category.objects.filter(published=True)
        #queryset = self.get_queryset()
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'Posts': serializer.data}, status=status.HTTP_200_OK)
      except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def retrieve(self, request,*args, **kwargs):
      try:
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'Post': serializer.data}, status=status.HTTP_200_OK)
      except Exception:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
