from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewSet(ModelViewSet):
  serializer_class = CategorySerializer
  #queryset = Category.objects.all()
  #agregar filtros
  #queryset = Category.objects.filter(published=True)
  permission_classes = [IsAdminOrReadOnly]
  #lookup_field = 'slug'
  # agregar libreria de filtrado
  filter_backends = [DjangoFilterBackend]
  # agregar campos de filtrado
  filterset_fields = ['slug', 'published']
  
  # sobreescribir metodo get_queryset, en cada peticion se ejecuta
  def get_queryset(self):
    user = self.request.user
    # si es super usuario, se listan todas las categorias
    if user.is_superuser:
        return Category.objects.all()
    # si no es super usuario, se listan solo las categorias publicadas
    else:
        return Category.objects.filter(published=True)
  
  #definir respuestas a los metodos http
  def create(self, request,*args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Category created successfully'}, status=status.HTTP_201_CREATED)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request,*args, **kwargs):
    # siempre se debe valdar una respuesta con detail, si no envia id
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance, data=request.data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Category updated successfully'})
    except Exception  as e:
      return Response({'error': f'Cannot update category. {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, *args, **kwargs ):
    # siempre se debe valdar una respuesta con detail, si no envia id
    try:
      instance = self.get_object()
      instance.delete()
      return Response({'message': 'Category deleted successfully'}, status=status.HTTP_200_OK)
    except Exception  as e:
      return Response({'error': f'Cannot delete category. {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        
  def list(self, request,*args, **kwargs):
    try:
      #queryset = Category.objects.filter(published=True)
      #queryset = self.get_queryset()
      queryset = self.filter_queryset(self.get_queryset())
      serializer = self.get_serializer(queryset, many=True)
      return Response({'categories': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
  def retrieve(self, request,*args, **kwargs):
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      return Response({'category': serializer.data}, status=status.HTTP_200_OK)
    except Exception:
      return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
