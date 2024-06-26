# Generated by Django 4.2.11 on 2024-05-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название курса')),
                ('type_cours', models.CharField(max_length=20, verbose_name='Тип курса')),
                ('period', models.CharField(max_length=25, verbose_name='Период курса')),
                ('exp', models.CharField(max_length=25, verbose_name='Требуемый опыт')),
                ('description', models.TextField(verbose_name='Описание курса')),
                ('price_in_month', models.IntegerField(verbose_name='Цена курса за месяц')),
                ('full_price', models.IntegerField(verbose_name='Полная цена курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
