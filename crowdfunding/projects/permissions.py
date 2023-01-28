from rest_framework import permissions

#making a custom permission so that only the owner of a project can edit it:
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #is the logged in user the owner
            return True
        return obj.owner == request.user #if that's true - then can edit

#making a custom permission so that only the creator of a pledge can edit it:
class IsSupporterOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #is the logged in user the owner
            return True
        return obj.supporter == request.user #if that's true - then can edit