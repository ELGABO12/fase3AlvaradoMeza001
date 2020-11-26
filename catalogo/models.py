from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


class Genre(models.Model):
    #Model representing a book genre."""
	name = models.CharField(max_length=200)
	summary = models.TextField(max_length=1000)

	class Meta:
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('genre-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.name


class Game(models.Model):
    
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	title = models.CharField(max_length=200)
	developer = models.TextField(max_length=200)
	editor= models.TextField(max_length=200)
	summary = models.TextField(max_length=1000, help_text='Deja descripcion del Juego')
	genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=False)
	image = models.ImageField(upload_to='imgs/', null=True, blank=True)
    
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('game-detail', args=[str(self.id)])