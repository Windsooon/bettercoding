from django.db import models
from problems.models import Problem


class Resources(models.Model):
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name='resources')
    name = models.CharField(max_length=512)
    url = models.URLField(max_length=512)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_time',)

# Create your models here.
