from django.db import models

class Courses(models.Model):
    title = models.CharField('Название курса', max_length=50)
    type_cours = models.CharField('Тип курса', max_length=20)
    period = models.CharField('Период курса', max_length=25)
    exp = models.CharField('Требуемый опыт', max_length=25)
    description = models.TextField('Описание курса')
    price_in_month = models.IntegerField('Цена курса за месяц')
    full_price = models.IntegerField('Полная цена курса')
    content = models.TextField('Содержание курса', default='Default content')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/courses/{self.id}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField('Название урока', max_length=200)
    content = models.TextField('Содержание урока')
    order = models.PositiveIntegerField('Порядок')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}: {self.title}"