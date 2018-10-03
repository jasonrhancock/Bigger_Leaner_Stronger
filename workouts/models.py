from django.db import models
from django.utils import timezone

# Create your models here.
class Workout(models.Model):
    lifter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    exercise = models.CharField(max_length=50)
    weight = models.CharField(max_length=4)
    reps_Set_1 = models.IntegerField(default=0)
    reps_Set_2 = models.IntegerField(default=0)
    reps_Set_3 = models.IntegerField(default=0)
    lifted_date = models.DateTimeField(
        blank=True, null=True)
    notes = models.TextField()

    def publish(self):
        self.lifted_date = timezone.now()
        self.save()

    def __str__(self):
        return self.exercise
