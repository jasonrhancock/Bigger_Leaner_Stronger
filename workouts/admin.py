from django.contrib import admin

# Register your models here.
from workouts.models import Workout, Exercise, Sets, ExerciseType
### PS: always better to use the full reference for import

class SetsInline(admin.TabularInline):
    model = Sets

class ExerciseInline(admin.TabularInline):
    model = Exercise
    # inlines = [SetsInline]

class WorkoutAdmin(admin.ModelAdmin):
    model = Workout
    fields = ('lifter',)
    readonly_fields = ('date',)
    inlines = [ExerciseInline, SetsInline]

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(ExerciseType)
