from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOnly(BasePermission):
    """
    Somente usuários do grupo Admin podem acessar.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name='Admin').exists()
        )


class IsPesquisadorOnly(BasePermission):
    """
    Somente usuários do grupo Pesquisador podem acessar.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name='Pesquisador').exists()
        )


class IsUsuarioOnly(BasePermission):
    """
    Usuário comum autenticado.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name='Usuario').exists()
        )


class AdminOrPesquisadorCanEdit(BasePermission):
    """
    - Admin e Pesquisador podem CRIAR / EDITAR / DELETAR
    - Qualquer usuário autenticado pode apenas VISUALIZAR (GET)
    """

    def has_permission(self, request, view):

        # Métodos de leitura liberados para qualquer usuário logado
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Métodos de escrita apenas para Admin ou Pesquisador
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.groups.filter(name='Admin').exists()
                or request.user.groups.filter(name='Pesquisador').exists()
            )
        )

