from django.urls import path
from .views import LoginView, RefreshTokenView

urlpatterns = [
    path('signin/', LoginView.as_view(), name='signin'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh')
]
