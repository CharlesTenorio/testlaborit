from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=150, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
