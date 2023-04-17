from django.db import models


class Сurrency(models.Model):
    usd = models.FloatField(verbose_name='usd')
    eur = models.FloatField(verbose_name='eur')
    date = models.DateField(
        auto_now_add=True, db_index=True, unique=True, verbose_name='Дата')

    def __str__(self):
        return 'Курсы USD и EUR'
