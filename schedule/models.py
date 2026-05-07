from django.db import models
from users.models import User

class DaySchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    ai_plan = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Schedule - {self.created_at.date()}"

class ScheduleTask(models.Model):
    schedule = models.ForeignKey(DaySchedule, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    time = models.TimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    category = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.time} - {'Completed' if self.is_done else 'Pending'}"