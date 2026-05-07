from django.db import models
from users.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=255)
    scheduled_time = models.TimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.user.username})"
    
class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()
    completed = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Completed' if self.completed else 'Missed'}"