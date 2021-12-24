from rest_framework.permissions import BasePermission

# sino es admin solo podra leer
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method=='GET':
            return True
        else:
            return request.user.is_staff
