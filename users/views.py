from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .models import User


class UserListCreateView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# /users/<id>
class UserGetUpdateDeleteView(generics.GenericAPIView):
    queryset = User.objects
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'delete']

    def get(self, request, id):
        record = get_object_or_404(
            self.queryset, pk=id
        )
        serializer = self.serializer_class(record, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        record = get_object_or_404(
            self.queryset, pk=id
        )
        serializer = self.serializer_class(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        pass
