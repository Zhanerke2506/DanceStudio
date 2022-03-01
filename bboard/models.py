from django.db import models

class Bb(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    info = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)