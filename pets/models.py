from django.db import models
from django.conf import settings

class Pet(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pets',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    colour = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pets/')

    def __str__(self):
        return self.name
