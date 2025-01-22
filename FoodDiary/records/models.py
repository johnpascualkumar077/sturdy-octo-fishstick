from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class MealRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    food_name = models.CharField(max_length=200)
    calories = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='meal_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.food_name} ({self.user.username})"
