from rest_framework.viewsets import ModelViewSet
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from rest_framework import status
from rest_framework.response import Response
# filtrado
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
# permisos
from comments.api.permissions import IsOwnerOrReadOnly

class CommentViewSet(ModelViewSet):
  serializer_class = CommentSerializer
  #filtrado
  filter_backends = [DjangoFilterBackend, OrderingFilter]
  filterset_fields = ['post', 'user', 'created_at']
  # ordenamiento de los resultados, por defecto es ascendente
  # con el signo menos se ordena de forma descendente
  OrderingFilter = ['-created_at']
  # permisos
  permission_classes = [IsOwnerOrReadOnly]

  #? sobreescribir metodo get_queryset, en cada peticion se ejecuta
  def get_queryset(self):
    user = self.request.user
    # si es super usuario, se listan todas las categorias
    if user.is_superuser:
        return Comment.objects.all()
    # si no es super usuario, se listan solo las categorias publicadas
    else:
        return Comment.objects.filter(state=True)
      
  #? definir respuestas a los metodos http
  def create(self, request,*args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Comment created successfully'}, status=status.HTTP_201_CREATED)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request,*args, **kwargs):
    # siempre se debe valdar una respuesta con detail, si no envia id
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance, data=request.data, partial=True)
      if serializer.is_valid():
        serializer.save()   
        return Response({'message': 'Comment updated successfully'})
    except Exception  as e:
      return Response({'error': f'Cannot update Comment. {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, *args, **kwargs ):
    # siempre se debe valdar una respuesta con detail, si no envia id
    try:
      instance = self.get_object()
      instance.delete()
      return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_200_OK)
    except Exception  as e:
      return Response({'error': f'Cannot delete Comment. {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        
  def list(self, request,*args, **kwargs):
    try:
      queryset = self.filter_queryset(self.get_queryset())
      serializer = self.get_serializer(queryset, many=True)
      return Response({'Comments': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
  def retrieve(self, request,*args, **kwargs):
    try:
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      return Response({'Comment': serializer.data}, status=status.HTTP_200_OK)
    except Exception:
      return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
