from django.db import models
from categories.models import Category
from courses.models import Courses


class Level(models.Model):
    LEVEL_CHOICES = (
        (0, 'Low'),
        (1, 'High'),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='level')
    courses = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        related_name='level')
    level = models.IntegerField(
        choices=LEVEL_CHOICES, default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level

    class Meta:
        ordering = ('create_time',)
