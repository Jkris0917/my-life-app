from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Habit, HabitLog
from .serializers import HabitSerializer, HabitLogSerializer

# Create your views here.
class HabitViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HabitSerializer
    
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
class HabitLogViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HabitLogSerializer
    
    def get_queryset(self):
        return HabitLog.objects.filter(habit__user=self.request.user)