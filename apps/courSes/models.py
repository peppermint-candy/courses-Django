from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Courses(models.Model):
	course = models.CharField(max_length=40)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

