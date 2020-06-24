from django.db import models

class Chambre(models.Model):
	CITES = ((1, 'Cité 1'), (2, 'Cité 2'), (3, 'Cité 3'))
	GENRES = ((1, 'Garçons'), (2, 'Filles'))
	name = models.CharField(max_length=4)
	num = models.CharField(max_length=5)
	cite = models.IntegerField(choices=CITES, default=1)
	genre = models.IntegerField(choices=GENRES, default=1)
	is_taken = models.BooleanField(default=False)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.num

