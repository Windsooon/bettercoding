# Generated by Django 2.0.6 on 2018-07-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problem_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='problem_id',
            field=models.IntegerField(default=1),
        ),
    ]
