# Generated by Django 4.2 on 2023-04-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Сurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.FloatField(verbose_name='usd')),
                ('eur', models.FloatField(verbose_name='eur')),
                ('date', models.DateField(auto_now_add=True, db_index=True, unique=True, verbose_name='Дата')),
            ],
        ),
    ]