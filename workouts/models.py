from django.db import models
from django.core.validators import MaxValueValidator
from django import forms


# Workout
    # Exercise
        # Set
class Workout(models.Model):
    lifter = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='workouts')
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    
# Create your models here.
class Exercise(models.Model):
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    exercise_type = models.ForeignKey('ExerciseType', on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return '{} -- {} -- {}'.format(self.lifter, self.exercise, self.lifted_date)

class Set(models.Model):
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='sets')
    weight = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(1500)])
    reps = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(50)])

class ExerciseType(models.Model):
    """Keep track of the supported exercises. Allows for generation of
        workouts and reporting on dem gainz"""
    name = models.CharField(max_length=50)
    # eventually the muscle_group can be its own model as well to further refine
    muscle_group = models.CharField(max_length=90)

    def __str__(self):
        return self.name
