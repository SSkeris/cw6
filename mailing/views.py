from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Mailing, Client, Log, Message


class ClientListView(ListView):
    """Список всех клиентов"""
    model = Client


class ClientCreateView(CreateView):
    """Класс для создания клиента"""
    model = Client
    fields = ('FIO', 'email', 'description')

    def get_success_url(self):
        return reverse('clients_list')


class ClientUpdateView(UpdateView):
    """Класс для редактирования клиента"""
    model = Client
    fields = ('FIO', 'email', 'description')

    def get_success_url(self):
        return reverse('clients_list')


class MailingListView(ListView):
    """Класс для отображения списка рассылок"""
    model = Mailing


class MailingDetailView(DetailView):
    """Класс для отображения одной рассылки"""
    model = Mailing


class MailingCreateView(CreateView):
    """Класс для создания рассылки"""
    model = Mailing
    fields = ('name', 'description', 'periodicity', 'start_date', 'end_date', 'clients')
    success_url = reverse_lazy('mailing_list')


class MailingUpdateView(UpdateView):
    """Класс для редактирования рассылки"""
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailing_detail')

    def get_success_url(self):
        """Перенаправляет на страницу с рассылкой"""
        return reverse('mailing_detail', args=[self.object.pk])


class MailingDeleteView(DeleteView):
    """Класс для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing_list')


class MessageListView(ListView):
    """Список просмотра всех сообщений"""
    model = Message


class MessageCreateView(CreateView):
    """Класс для создания сообщения"""
    model = Message
    fields = ('title', 'text', 'mailing_list')

    def get_success_url(self):
        return reverse('message_list')


class MessageUpdateView(UpdateView):
    """Класс для редактирования сообщения"""
    model = Message
    fields = ('title', 'text', 'mailing_list')

    def get_success_url(self):
        return reverse('message_list')


class LogListView(ListView):
    """Класс для отображения списка логов"""
    model = Log

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = context_data['object_list'].count()
        context_data['success'] = context_data['object_list'].filter(status=True).count()
        context_data['error'] = context_data['object_list'].filter(status=False).count()

        return context_data
