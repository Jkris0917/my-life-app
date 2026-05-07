from rest_framework.routers import DefaultRouter
from .views import DayScheduleViewSet, ScheduleTaskViewSet, generate_ai_plan
from django.urls import path


router = DefaultRouter()
router.register(r'day-schedules', DayScheduleViewSet, basename='day-schedule')
router.register(r'schedule-tasks', ScheduleTaskViewSet, basename='schedule-task')

urlpatterns = router.urls + [
    path('generate-schedule/',generate_ai_plan, name='generate-schedule'),
]