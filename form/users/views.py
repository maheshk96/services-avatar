from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .producer import publish
from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request): #api/users
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('user_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #api/user/id
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None): #api/user/id
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('user_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #api/user/id
        user = User.objects.get(id=pk)
        user.delete()
        publish('user_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)