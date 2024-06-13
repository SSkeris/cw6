from django.db import models

from users.models import User

# from mailing.models import Message

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """Клиент"""
    FIO = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=150, verbose_name='Почта', unique=True)
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.FIO} {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('FIO',)


class Message(models.Model):
    """Сообщение для рассылки"""
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    """Рассылка и её параметры"""
    FIVE_MINUTES = "Каждые пять минут"
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (FIVE_MINUTES, "Каждые пять минут"),
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание', help_text='не обязательное поле')
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default=CREATED, verbose_name='Статус')
    periodicity = models.CharField(max_length=150, choices=PERIODICITY_CHOICES,
                                   default=DAILY, verbose_name='Периодичность')
    start_date = models.DateTimeField(verbose_name='Дата начала', **NULLABLE,
                                      help_text='(формат 11.05.2024) не обязательное поле')
    end_date = models.DateTimeField(verbose_name='Дата окончания', **NULLABLE, help_text='не обязательное поле')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)

    clients = models.ManyToManyField(Client, verbose_name='Клиенты для рассылки')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.status}, время работы: {self.start_date} - {self.end_date}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('name',)
        permissions = [
            ('deactivate_mailing', 'Can deactivate mailing'),
            ('view_all_mailings', 'Can view all mailings'),
        ]


class Log(models.Model):
    """Лог рассылки"""
    time = models.DateTimeField(verbose_name='Дата и время попытки отправки', auto_now_add=True)
    status = models.BooleanField(verbose_name='Статус попытки отправки')
    server_response = models.CharField(max_length=150, verbose_name='Ответ сервера почтового сервиса', **NULLABLE)

    mailing_list = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self):
        return f'{self.client} {self.mailing_list} {self.time} {self.status} {self.server_response}'

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылок'
