from django.db import models

class Follow(models.Model):
    follower_id = models.IntegerField()   
    following_id = models.IntegerField()  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower_id', 'following_id')  # Para evitar duplicados

    def __str__(self):
        return f"{self.follower_id} follows {self.following_id}"

