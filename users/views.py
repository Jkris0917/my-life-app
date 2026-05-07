from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)