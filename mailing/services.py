import smtplib
from datetime import datetime, timedelta

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing, MailingAttempts


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    print(f'локальное время: {current_datetime}\nзона: {zone}')
    mailings = Mailing.objects.all()
    print(f'Количество рассылок для отправки автоматически: {mailings.count()}')

    for mailing in mailings:
        print(f'Рассылка ID: {mailing.id}, next_send_time: {mailing.next_send_time}')
        mailing.status = Mailing.STARTED
        clients = mailing.clients.all()
        try:
            server_response = send_mail(
                subject=mailing.message.title,
                message=mailing.message.text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in clients],
                fail_silently=False,
            )
            print(mailing.next_send_time)
            print(f'ответ сервера: {server_response}')
            MailingAttempts.objects.create(last_attempt_time=current_datetime,
                                           status=MailingAttempts.SUCCESS,
                                           server_response=server_response,
                                           mailing=mailing, )
        except smtplib.SMTPException as e:
            MailingAttempts.objects.create(last_attempt_time=current_datetime,
                                           status=MailingAttempts.FAIL,
                                           server_response=str(e),
                                           mailing=mailing,
                                           )

        if mailing.periodicity == 'daily':
            mailing.next_send_time += timedelta(days=1)
        elif mailing.periodicity == 'weekly':
            mailing.next_send_time += timedelta(weeks=1)
        elif mailing.periodicity == 'monthly':
            mailing.next_send_time += timedelta(days=30)
        mailing.save()
        print(f'Обновленное next_send_time для рассылки ID: {mailing.id}: {mailing.next_send_time}')


def start_scheduler():
    print('Starting scheduler...')
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=10)

    if not scheduler.running:
        scheduler.start()

    print('Scheduler started')
