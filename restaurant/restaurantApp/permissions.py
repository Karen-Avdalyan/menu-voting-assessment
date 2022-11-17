"""
herre writen all base permission checkings also if you will need some individual
checking create class and provide your checking methods (each class have specific checking logic)
for e.g. IsAuthorizedForMenu class we have all checkings about authorization for menu
"""
import datetime

from rest_framework.permissions import BasePermission


class IsAuthorizedForMenuListCreation(BasePermission):
    def has_create_permission(self, request, view):
        return self.has_alter_permission(request, view)

    def has_alter_permission(self, request, view):
        serializer = view.serializer_class(data=request.data)
        if serializer.is_valid():
            restaurant = serializer.validated_data.pop("restaurant_id")
            if request.user == restaurant.manager:
                return True
            else:
                return False
        return True

    def has_get_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_permission(self, request, view):
        if request.method == 'POST':
            return self.has_create_permission(request, view)
        if request.method == 'GET':
            return self.has_get_permission(request, view)
        return False

class IsAuthorizedForMenuAlter(BasePermission):
    def has_alter_permission(self, request, view):
        menu = view.get_object()
        return request.user == menu.restaurant.manager

    def has_update_permission(self, request, view):
        return self.has_alter_permission(request, view)

    def has_get_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_delete_permission(self, request, view):
        return self.has_alter_permission(request, view)

    def has_permission(self, request, view):
        if request.method == 'GET':
            return self.has_get_permission(request, view)
        if request.method == 'PUT':
            return self.has_update_permission(request, view)
        if request.method == 'PATCH':
            return self.has_update_permission(request, view)
        if request.method == 'DELETE':
            return self.has_delete_permission(request, view)
        return False


class IsAuthorizedForMenuVoting(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.groups.filter(pk=1) and
            request.user.employee.last_voted < datetime.date.today()
        )


class CanAlterVote(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user.employee)

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.groups.filter(pk=1)
        )


class IsAuthorizedForRestaurant(BasePermission):
    def has_create_permission(self, request, view):
        return self.has_alter_permission(request, view)

    def has_alter_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

    def has_update_permission(self, request, view):
        return self.has_alter_permission(request, view)

    def has_get_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_delete_permission(self, request, view):
        return self.has_alter_permission(request, view)

    def has_permission(self, request, view):
        if request.method == 'POST':
            return self.has_create_permission(request, view)
        if request.method == 'GET':
            return self.has_get_permission(request, view)
        if request.method == 'PUT':
            return self.has_update_permission(request, view)
        if request.method == 'PATCH':
            return self.has_update_permission(request, view)
        if request.method == 'DELETE':
            return self.has_delete_permission(request, view)
        return False
