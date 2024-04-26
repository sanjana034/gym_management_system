from django.db import models

from apps.authentication.models import CustomUser

class GymPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_name = models.TextField(max_length=50)
    plan_duration = models.CharField(max_length=50, blank=False, null=False)
    plan_cost = models.FloatField()
    
    def __str__(self) -> str:
        return self.plan_name

    
class UserBooking(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan_type = models.ForeignKey(GymPlan, on_delete=models.DO_NOTHING, blank=False, null=False)
    start_date = models.DateField(auto_now=True)


class UserActivity(models.Model):
    activity_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_logged = models.DateField(auto_now=True)
    tracked_weight = models.FloatField()


class ClassSchedule(models.Model):
    class_id = models.BigAutoField(primary_key=True)
    tutor_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    class_name = models.CharField(max_length=50, blank=False, null=False)
    class_description = models.TextField(max_length=500, blank=True, null=True)
    class_date = models.DateTimeField(auto_now=False, null=False, blank=False)


class Feedback(models.Model):
    feedback_id = models.BigAutoField(primary_key=True)
    feedback_msg = models.TextField(max_length=500, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)