from django.db import models

class PlayerScore(models.Model):
    player_name = models.CharField(max_length=255)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player_name} - {self.score}"
