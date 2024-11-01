from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120, write_only=True)
    password = serializers.CharField(max_length=60, write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        # Validar que el usuario exista
        if not user:
            raise AuthenticationFailed('Invalid username or password')

        # Validar que el usuario este activo
        if not user.is_active:
            raise AuthenticationFailed(f'User {username} is inactive')

        token = RefreshToken.for_user(user)

        return {
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        }
