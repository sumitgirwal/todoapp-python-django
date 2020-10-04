from django.db import models

class Task(models.Model):
    text   = models.CharField(max_length=200, null=True)
    """docstring for Task"""
    def __str__(self):
        data = str(self.id)+"-"+str(self.text)
        return data

