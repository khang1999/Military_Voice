from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Recording(models.Model):
	fileName = models.CharField(max_length = 100)
	textid = models.IntegerField()
	text = models.CharField(max_length = 100)
	audiofile = models.FileField(upload_to="recordings/")
	verified = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])

	def __str__(self):
		return self.fileName