from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Workout(models.Model):
    lifter = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='workouts')
    # TODO: Figure out why the exercise shows up as 'Exercise Object (1)'
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(1500)])
    reps_Set_1 = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(50)])
    reps_Set_2 = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(50)])
    reps_Set_3 = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(50)])
    lifted_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return '{self.lifter} -- {self.exercise} -- {self.lifted_date}'.format(self.lifter,
                                                                               self.exercise,
                                                                               self.lifted_date)


class Exercise(models.Model):
    """Keep track of the supported exercises. Allows for generation of
        workouts and reporting on dem gainz"""
    name = models.CharField(max_length=50)
    # eventually the muscle_group can be its own model as well to further refine
    muscle_group = models.CharField(max_length=90)
