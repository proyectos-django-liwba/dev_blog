from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
  def has_permission(self, request, view):
    # si la peticion es de solo lectura, se permite
    if request.method in ['GET', 'HEAD', 'OPTIONS']:
      return True
    
    # si la peticion es de escritura, se valida si es admin
    return request.user.is_staff