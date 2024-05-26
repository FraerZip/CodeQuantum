from django.db import models


class Courses(models.Model):
    title = models.CharField('Название курса', max_length=50)
    type_cours = models.CharField('Тип курса', max_length=20)
    period = models.CharField('Период курса', max_length=25)
    exp = models.CharField('Требуемый опыт', max_length=25)
    description = models.TextField('Описание курса')
    price_in_month = models.IntegerField('Цена курса за месяц')
    full_price = models.IntegerField('Полная цена курса')

    # img =
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
