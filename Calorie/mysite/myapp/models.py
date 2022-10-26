from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class food(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length = 100)
    carbs = models.FloatField()
    protien = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

class consume(models.Model):
    # def __str__(self):
    #     return self.user
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(food,on_delete=models.CASCADE)