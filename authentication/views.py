from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import generics
from .serializers import LoginSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data
        return Response(tokens, status=status.HTTP_200_OK)
