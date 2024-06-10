# Generated by Django 5.0.4 on 2024-05-11 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_log_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='description',
            field=models.TextField(blank=True, help_text='не обязательное поле', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата начала'),
        ),
    ]
