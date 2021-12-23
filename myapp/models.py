from django.db import models

class Online(models.Model):

	domain = models.CharField(max_length = 30)

	class Meta:
		db_table = "online"

class Dreamreal(models.Model):

	website = models.CharField(max_length = 50)
	mail = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	phonenumber = models.IntegerField()

	class Meta:
		db_table = "dreamreal"

