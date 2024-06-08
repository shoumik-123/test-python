# from django.http import HttpResponse
# from django.shortcuts import render
# from .email_utils import send_email
#
#
# def machine(request):
#     return render(request, 'Teacher/machine.html')
#
#
# def deep(request):
#     return render(request,'Teacher/deep.html')
#
#
# def contact_view(request):
#     if request.method == 'POST':
#         subject = request.POST.get('subject', 'No Subject')
#         message = request.POST.get('message', '')
#         recipient_email = request.POST.get('email', '')
#
#         if subject and message and recipient_email:
#             send_email(
#                 subject,
#                 message,
#                 [recipient_email],
#             )
#             return render(request, 'Teacher/contact_success.html')
#     return render(request, 'Teacher/contact_form.html')
#
#
# def login(request):
#     return render(request, 'registration/login.html')
#
#
# def PasswordResetView(request):
#     return render(request, 'registration/password_reset_form.html')
#
#
# def PasswordResetDoneView(request):
#     return render(request, 'registration/password_reset_done.html')
#
#
# def PasswordResetConfirmView(request):
#     return render(request, 'registration/password_reset_confirm.html')
#
#
# def PasswordResetCompleteView(request):
#     return render(request, 'registration/password_reset_complete.html')
#
#

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


def machine(request):
    return render(request, 'Teacher/machine.html')


def deep(request):
    return render(request, 'Teacher/deep.html')


def contact_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message', '')
        recipient_email = request.POST.get('email', '')

        if subject and message and recipient_email:
            from .email_utils import send_email
            send_email(
                subject,
                message,
                [recipient_email],
            )
            return render(request, 'Teacher/contact_success.html')
    return render(request, 'Teacher/contact_form.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            login_email = request.POST.get('username', '')
            send_login_email(login_email)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@receiver(user_logged_in)
def send_login_email(sender, user, request, **kwargs):
    # Send login alert email
    send_mail(
        'Login Alert',
        f'User with email {user.email} has logged in.',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )


password_reset_view = auth_views.PasswordResetView.as_view(
    template_name='registration/password_reset_form.html'
)

password_reset_done_view = auth_views.PasswordResetDoneView.as_view(
    template_name='registration/password_reset_done.html'
)

password_reset_confirm_view = auth_views.PasswordResetConfirmView.as_view(
    template_name='registration/password_reset_confirm.html'
)

password_reset_complete_view = auth_views.PasswordResetCompleteView.as_view(
    template_name='registration/password_reset_complete.html'
)
