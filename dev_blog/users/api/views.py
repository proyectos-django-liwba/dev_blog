from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import (
  UserRegisterSerializer,
  UserSerializer, 
  UserUpdateSerializer,
  UserChangePasswordSerializer,
)
from users.models import User


class RegisterView(APIView):
  #endpoint para registrar usuarios
    def post(self, request):
      # leer los datos del request
      serializer = UserRegisterSerializer(data=request.data)
      # validar los datos
      if serializer.is_valid(raise_exception=True):
        # guardar
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data={"message":"Usuario creado correctamente", "user":serializer.data})
      
      return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":serializer.errors, "message":"No se pudo crear el usuario"})
    
  
class UserView(APIView):
  
  # seguridad para el endpoint, solo usuarios autenticados
  permission_classes = [IsAuthenticated]
  
  # obtener el usuario autenticado, se debe agregar un header con el token, "bearer <token>"
  def get(self, request):
    serializer = UserSerializer(request.user)
    
    # validar los datos
    if serializer is not None:
      # retornar los datos del usuario
      return Response(status=status.HTTP_200_OK, data={"user":serializer.data})
    
    return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":serializer.errors, "message":"El token es inválido"})
  
  # actualizar usuario autenticado
  def put(self, request):
    # obtener datos del usuario autenticado
    user = User.objects.get(id=request.user.id)
    # se agregan los nuevos datos y los datos anteriores
    serializer = UserUpdateSerializer(user, request.data)
    
    # validar los datos
    if serializer.is_valid(raise_exception=True):
      # guardar
      serializer.save()
      return Response(status=status.HTTP_200_OK, data={"message":"Usuario actualizado correctamente", "user":serializer.data})
    
    return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":serializer.errors, "message":"No se pudo actualizar el usuario"})
  
class UserChangePasswordView(APIView):
  
  # seguridad para el endpoint, solo usuarios autenticados
  permission_classes = [IsAuthenticated]
  
  # actualizar usuario autenticado
  def put(self, request):
    # obtener datos del usuario autenticado
    user = User.objects.get(id=request.user.id)
    # se agregan los nuevos datos y los datos anteriores
    serializer = UserChangePasswordSerializer(user, request.data)
    
    # validar los datos
    if serializer.is_valid(raise_exception=True):
      # guardar
      serializer.save()
      return Response(status=status.HTTP_200_OK, data={"message":"Contraseña actualizada correctamente", "user":serializer.data})
    
    return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":serializer.errors, "message":"No se pudo actualizar la contraseña"})      
    