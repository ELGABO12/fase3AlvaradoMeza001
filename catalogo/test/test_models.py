from django.test import TestCase
from .models import Genre, Game

class GenreModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Genre.objects.create(name='Social', summary='Prueba')
    
    def test_name_label(self):
        genre=Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_summary_label(self):
        genre=Genre.objects.get(id=1)
        field_label = genre._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_name_max_length(self):
        genre=Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length,100)
    
    def test_summary_max_length(self):
        genre=Genre.objects.get(id=1)
        max_length = genre._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)
        
    def test_get_absolute_url(self):
        genre=Genre.objects.get(id=1)
        self.assertEquals(genre.get_absolute_url(), '/catalogo/genre/1')

class GameModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        g = Genre.objects.create(name='Social', summary='Prueba')
        test_game = Game.objects.create(id= '01', title='Among Us', summary='Prueba', genre=g )
    
    def test_title_label(self):
        game= Game.objects.get(id= '01')
        field_label = game._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_summary_label(self):
        game=Game.objects.get(id='01')
        field_label = game._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_genre_label(self):
        game=Game.objects.get(id='01')
        field_label = game._meta.get_field('genre').verbose_name
        self.assertEquals(field_label,'genre')
    
    def test_title_max_length(self):
        game=Game.objects.get(id='01')
        max_length = game._meta.get_field('title').max_length
        self.assertEquals(max_length,200)
    
    def test_summary_max_length(self):
        game=Game.objects.get(id='01')
        max_length = game._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)
