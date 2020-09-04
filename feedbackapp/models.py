from django.db import models
from django.utils import timezone

# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=254)
    message = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.mail
