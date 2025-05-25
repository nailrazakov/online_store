from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserForm
from django.core.mail import send_mail
from django.contrib.auth import login


def send_welcome_email(user_email):
    subject = 'Добро пожаловать в наш сервис'
    message = 'Спасибо, что зарегистрировались в нашем сервисе'
    from_email = 'newsletter82@mail.ru'
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        send_welcome_email(user.email)
        return super().form_valid(form)
