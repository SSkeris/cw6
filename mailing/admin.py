from django.contrib import admin

from mailing.models import Client, Message, Mailing, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'email', 'pk',)
    list_filter = ('FIO', 'email',)
    search_fields = ('FIO', 'email', 'description',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'status', 'periodicity', 'start_date', 'end_date',)
    list_filter = ('name', 'status', 'periodicity', 'clients', 'start_date', 'end_date',)
    search_fields = ('name', 'description',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'mailing_list',)
    list_filter = ('title', 'mailing_list',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mailing_list', 'server_response', 'client', 'time', 'status',)
    list_filter = ('mailing_list', 'server_response', 'client', 'time', 'status',)
