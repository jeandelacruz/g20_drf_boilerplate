from django.urls import path
from .views import LoginView

urlpatterns = [
    path('signin/', LoginView.as_view(), name='signin')
]
