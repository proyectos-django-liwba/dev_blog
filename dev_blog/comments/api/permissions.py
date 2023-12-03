from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadOnly(BasePermission):
  def has_object_permission(self, request, view, obj):
      # cualquier usuario puede leer y crear un comentario
    if request.method == 'GET' or request.method == 'POST':
        print('GET or POST')
        return True
    else:
        # si quiere eliminar o editar un comentario, debe ser el dueño
        id_comment = view.kwargs['pk']
        comment = Comment.objects.get(pk=id_comment)
        id_user = request.user.pk
        id_user_comment = comment.user_id
        
        # si el id del usuario logueado es igual al id del usuario que creo el comentario
        if id_user == id_user_comment:
            return True # puede eliminar o editar
        
        # por defecto no puede eliminar o editar
        return False # no puede eliminar o editar
