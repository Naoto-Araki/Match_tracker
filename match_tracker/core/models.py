from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.username if not self.nickname else self.nickname
    
class GameType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Match(models.Model):
    player1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='player1_matches')
    player2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='player2_matches')
    winner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='won_matches')
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.player1} vs {self.player2} - {self.game_type.name} - {self.date}"
    
class Friendship(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friends_of')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'friend')
    
    def __str__(self):
        return f"{self.user} → {self.friend}"
