from django.db import models
from categories.models import Category


class Problem(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='problem')
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=2048)
    true_answer = models.CharField(max_length=1048)
    wrong_answer1 = models.CharField(max_length=1048)
    wrong_answer2 = models.CharField(max_length=1048)
    wrong_answer3 = models.CharField(max_length=1048)
    have_code = models.BooleanField(default=False)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('create_time',)
