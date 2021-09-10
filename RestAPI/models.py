from django.db import models

class CRUDApi(models.Model):
	name = models.CharField(max_length=50, blank=False)
	collage = models.CharField(max_length=70, blank=False)
	gender = models.BooleanField()