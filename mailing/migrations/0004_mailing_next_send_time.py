# Generated by Django 4.2.2 on 2024-06-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_alter_mailing_periodicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='next_send_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
