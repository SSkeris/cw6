from django.contrib import admin

from mailing.models import Client, Message, Mailing, MailingAttempts


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'email', 'pk',)
    list_filter = ('FIO', 'email',)
    search_fields = ('FIO', 'email', 'description',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'status', 'periodicity', 'start_date', 'end_date',)
    list_filter = ('name', 'status', 'periodicity',)
    search_fields = ('name', 'description',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'owner',)
    list_filter = ('title',)


@admin.register(MailingAttempts)
class MailingAttemptsAdmin(admin.ModelAdmin):
    list_display = ('mailing',)
