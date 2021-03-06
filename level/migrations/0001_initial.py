# Generated by Django 2.0.6 on 2018-07-07 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(0, 'Low'), (1, 'High')], default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='categories.Category')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='courses.Courses')),
            ],
            options={
                'ordering': ('create_time',),
            },
        ),
    ]
