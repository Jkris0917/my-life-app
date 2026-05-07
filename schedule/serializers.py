from rest_framework import serializers
from .models import DaySchedule, ScheduleTask

class ScheduleTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleTask
        fields = ['id', 'schedule', 'title', 'time', 'is_done', 'category']
        
class DayScheduleSerializer(serializers.ModelSerializer):
    tasks = ScheduleTaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = DaySchedule
        fields = ['id', 'user', 'date', 'ai_plan', 'is_completed', 'created_at', 'tasks']