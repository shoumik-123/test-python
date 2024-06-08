from django.db import models


# Create your models here.
class Blog(models.Model):
    blog1 = models.CharField(max_length=30)
    blog2 = models.CharField(max_length=30)
    blog3 = models.CharField(max_length=30)
