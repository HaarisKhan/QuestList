from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='profile/icons/')

    def __str__(self):
        return self.username

    def update_address(self, address):
        self.address = address
        self.save()

    def change_icon(self, icon):
        self.icon = icon
        self.save()