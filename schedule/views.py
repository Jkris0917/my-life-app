from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import ScheduleTaskSerializer, DayScheduleSerializer
import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .ai_generator import generate_daily_schedule
from .models import DaySchedule, ScheduleTask
# Create your views here.

class ScheduleTaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ScheduleTaskSerializer
    
    def get_queryset(self):
        return ScheduleTask.objects.filter(schedule__user=self.request.user)

class DayScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DayScheduleSerializer
    
    def get_queryset(self):
        return DaySchedule.objects.filter(user=self.request.user)
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def generate_ai_plan(request):
    try:
        user = request.user
        user_data = {
            "wake_time": user.wake_time.strftime("%H:%M") if user.wake_time else None,
            "sleep_time": user.sleep_time.strftime("%H:%M") if user.sleep_time else None,
            "goals": user.goals,
        }
        today = datetime.date.today()
        ai_plan = generate_daily_schedule(user_data)
        schedule = DaySchedule.objects.create(user=user, date=today, ai_plan=ai_plan)
        return Response(
            {'message': 'AI plan generated successfully', 'date': today, 'ai_plan': ai_plan},
        )
    except Exception as e:
        return Response({'error': str(e)}, status=500)