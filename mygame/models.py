from turtle import ScrolledCanvas
from django.db import models

class Score(models.Model):
    points = models.IntegerField()
    player = models.CharField(max_length=3)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.player} Score: {self.points} @{self.timestamp}'