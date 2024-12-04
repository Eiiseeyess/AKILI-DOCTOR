from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    """Allow only the author of the article to edit or delete it."""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
