from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.TextField()
	description = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone
		self.save

	def __str__(self):
		return self.title
