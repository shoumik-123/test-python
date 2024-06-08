# # your_app/admin.py
#
# from django.conf import settings
# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
# from import_export.admin import ImportExportModelAdmin
# from .resources import UserResource
#
#
# class MyUserAdmin(ImportExportModelAdmin):
#     resource_class = UserResource
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
#
#     def save_model(self, request, obj, form, change):
#         if not change:
#             password = User.objects.make_random_password()
#             obj.set_password(password)
#             obj.save()
#             send_mail(
#                 'Your username and password for Metlinx',
#                 f'Username: {obj.username}\nPassword: {password}\nTHANK YOU.',
#                 settings.DEFAULT_FROM_EMAIL,
#                 [obj.email],
#                 fail_silently=False,
#             )
#         else:
#             obj.save()
#
#
# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from import_export.admin import ImportExportModelAdmin


class MyUserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

    def save_model(self, request, obj, form, change):
        if not change:
            password = User.objects.make_random_password()
            obj.set_password(password)
            obj.save()
            send_mail(
                'Your username and password for Metlinx',
                f'Username: {obj.username}\nPassword: {password} \n THANK YOU.',
                settings.DEFAULT_FROM_EMAIL,
                [obj.email],
                fail_silently=False,
            )
        else:
            obj.save()


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

