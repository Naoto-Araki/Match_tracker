from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

class GameType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    