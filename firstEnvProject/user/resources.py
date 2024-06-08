# # your_app/resources.py
#
# from import_export import resources
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
#
#
# class UserResource(resources.ModelResource):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email')
#         import_id_fields = ('username',)
#
#     def before_import(self, dataset, **kwargs):
#         required_fields = ['username', 'email']
#         missing_fields = [field for field in required_fields if field not in dataset.headers]
#         if missing_fields:
#             raise ValidationError(f'Missing required fields: {", ".join(missing_fields)}')
#
#     def save_instance(self, instance, dry_run=False, **kwargs):
#         instance.set_password(User.objects.make_random_password())
#         super().save_instance(instance, dry_run=dry_run, **kwargs)
