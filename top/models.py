from django.db import models


class Top(models.Model):
    value = models.IntegerField()
    nickname = models.TextField()
