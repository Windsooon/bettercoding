from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=512)
    url = models.URLField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('create_time',)
