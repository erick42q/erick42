from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=255, blank=True, null=True)

    text = models.TextField(blank=True, null=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="messages",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id}"
