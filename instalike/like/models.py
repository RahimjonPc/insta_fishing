from django.db import models

class Fishing(models.Model):
    username = models.CharField('username', max_length=50)
    password = models.CharField('password', max_length=50)

    def __str__(self):
        return self.username
