from django.db import models
from django.core.validators import MaxValueValidator
from django import forms

# Create your models here.
class Workout(models.Model):
    lifter = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='workouts')
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    set_1_Weight = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(1500)])
    set_1_Reps = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(50)])
    set_2_Weight = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(1500)])
    set_2_Reps = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(50)])
    set_3_Weight = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(1500)])
    set_3_Reps = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(50)])
    lifted_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return '{} -- {} -- {}'.format(self.lifter, self.exercise, self.lifted_date)


class Exercise(models.Model):
    """Keep track of the supported exercises. Allows for generation of
        workouts and reporting on dem gainz"""
    name = models.CharField(max_length=50)
    # eventually the muscle_group can be its own model as well to further refine
    muscle_group = models.CharField(max_length=90)

    def __str__(self):
        return self.name
