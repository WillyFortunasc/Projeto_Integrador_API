from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Admin').exists()


class IsPesquisador(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Pesquisador').exists()


class IsUsuario(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Usuario').exists()


class AdminOrPesquisadorCanEdit(BasePermission):
    """
    Admin e Pesquisador podem criar/editar.
    Usuario só pode visualizar.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # GET, HEAD, OPTIONS liberado para todos autenticados

        return request.user and request.user.is_authenticated and (
            request.user.groups.filter(name='Admin').exists() or
            request.user.groups.filter(name='Pesquisador').exists()
        )
