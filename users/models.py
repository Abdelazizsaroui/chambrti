from django.db import models
from django.contrib.auth.models import User
from chambres.models import Chambre

class Roommates(models.Model):
	GENRES = ((1, 'Garçons'), (2, 'Filles'))
	user1 = models.ForeignKey(User, related_name='roommate1', on_delete=models.CASCADE)
	user2 = models.ForeignKey(User, related_name='roommate2', on_delete=models.CASCADE)
	chambre = models.ForeignKey(Chambre, blank=True, null=True, on_delete=models.CASCADE, related_name='rommates_chambre')
	choices = models.TextField()
	updated_at = models.DateTimeField(auto_now=True)
	genre = models.IntegerField(choices=GENRES, default=1)
	valid = models.BooleanField(default=False)
	third = models.BooleanField(default=False)

	def __str__(self):
		return self.user1.get_full_name() + ' | ' + self.user2.get_full_name()

	def save(self, *args, **kwargs):
		if self.user1.groups.all().last().name == "third" or self.user2.groups.all().last().name == "third":
			self.third = True
		else:
			self.third = False
		if self.user1.groups.all().first().name == "boy":
			self.genre = 1
		else:
			self.genre = 2
		super(Roommates, self).save(*args, **kwargs)





