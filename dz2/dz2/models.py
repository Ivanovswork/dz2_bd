from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    surname = models.CharField(max_length=60, null=False, blank=False)
    middlename = models.CharField(max_length=60, null=False, blank=False)
    telephon_number = models.CharField(max_length=20, unique=True, null=True, blank=False)


