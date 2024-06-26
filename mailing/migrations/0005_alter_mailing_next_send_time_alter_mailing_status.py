# Generated by Django 4.2.2 on 2024-06-14 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_mailing_next_send_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='next_send_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'Завершена'), ('CREATED', 'Создана'), ('STARTED', 'Запущена')], default='Создана', max_length=150, verbose_name='Статус'),
        ),
    ]
