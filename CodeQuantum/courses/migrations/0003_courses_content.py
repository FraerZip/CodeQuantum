# Generated by Django 4.2.11 on 2024-06-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='content',
            field=models.TextField(default='Default content', verbose_name='Содержание курса'),
        ),
    ]