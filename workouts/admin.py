from django.contrib import admin

# Register your models here.
from workouts.models import Workout, Exercise
### PS: always better to use the full reference for import

admin.site.register(Workout)
admin.site.register(Exercise)
