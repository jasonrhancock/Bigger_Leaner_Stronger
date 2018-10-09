from django.contrib import admin

# Register your models here.
from workouts.models import Workout, Exercise, Set, ExerciseType
### PS: always better to use the full reference for import

class SetInline(admin.TabularInline):
    model = Set

class ExerciseInline(admin.TabularInline):
    model = Exercise
    inlines = [SetInline]

class WorkoutAdmin(admin.ModelAdmin):
    model = Workout
    fields = ('lifter',)
    readonly_fields = ('date',)
    inlines = [ExerciseInline]

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise)
admin.site.register(ExerciseType)
