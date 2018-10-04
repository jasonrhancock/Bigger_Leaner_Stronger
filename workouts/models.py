from django.db import models
from django.utils import timezone

# Create your models here.
class Workout(models.Model):
    lifter = models.ForeignKey('auth.User', on_delete=models.CASCADE, 
        related_name='workouts')
    # exercise = models.CharField(max_length=50)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, 
        related_name='workouts')
    weight = models.CharField(max_length=4) ### PS: porque no los IntegerField???
    reps_Set_1 = models.IntegerField(default=0)
    reps_Set_2 = models.IntegerField(default=0)
    reps_Set_3 = models.IntegerField(default=0)
    lifted_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True)
    ### PS: consider using `auto_now_add=True` in that DateTimeField rather than using the publish function to set the date to now. 
    notes = models.TextField()

    # def publish(self):
    #     self.lifted_date = timezone.now()
    #     self.save()

    def __str__(self):
        return f'{selflifter} -- {self.exercise} -- {self.lifted_date}'


class Exercise(models.Model):
    """Keep track of the supported exercises. Allows for generation of
        workouts and reporting on dem gainz"""
    name = models.CharField(max_length=50)
    # eventually the muscle_group can be its own model as well to further refine
    muscle_group = models.CharField(max_length=90)
