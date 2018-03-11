from rest_framework import permissions

class HasFieldLevelPermission(permissions.BasePermission):
    """
    Custom permission to only allow group members to change certain attrbutes
    """

    def has_object_permission(self, request, view, instance):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        for field_name, field_value in request.data.items():
            if field_value:
                if (
                    request.user.has_perm('read_{}_article'.format(field_name))
                    and request.method in permissions.SAFE_METHODS
                ):
                    return True
                elif (
                    request.user.has_perm('change_{}_article'.format(field_name))
                    and request.method not in permissions.SAFE_METHODS
                ):
                    return True

        return False
