from django.db import models
from django.core.validators import MaxValueValidator


class Workout(models.Model):
    lifter = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='workouts')
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return '{} -- {}'.format(self.lifter, self.date)


class Exercise(models.Model):
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    exercise_type = models.ForeignKey('ExerciseType', on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.exercise_type)


class Sets(models.Model):
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='sets')
    weight = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(1500)])
    reps = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(50)])

    def __str__(self):
        return '{} -- {} -- {}'.format(self.exercise, self.weight, self.reps)


class ExerciseType(models.Model):
    """Keep track of the supported exercises. Allows for generation of
        workouts and reporting on dem gainz"""
    name = models.CharField(default='None', max_length=50)
    # eventually the muscle_group can be its own model as well to further refine
    muscle_group = models.CharField(default='None', max_length=90)

    def __str__(self):
        return self.name
