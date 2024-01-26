from django.db import models

class PlayerScore(models.Model):
    player_name = models.CharField(max_length=255)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player_name} - {self.score}"
    

class Reports(models.Model):
    email = models.CharField(max_length=255)
    bug_title = models.CharField(max_length=255)
    bug_description = models.TextField()
    bug_steps = models.TextField()
    bug_type = models.CharField(max_length=255)
    bug_priority = models.CharField(max_length=255)