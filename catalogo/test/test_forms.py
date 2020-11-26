from django.test import TestCase
from .forms import GenreForm, GameForm
from .models import Genre, Game
from django.core.files.uploadedfile import SimpleUploadedFile

class GenreFormsTest(TestCase):
    def test_valid_form(self):
        g = Genre.objects.create(name='Social', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Genre.objects.create(name='', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertFalse(form.is_valid())

class GameFormsTest(TestCase):
    def test_valid_form(self):
        genre = Genre.objects.create(name='Social', summary='Prueba')
        genre = Genre.objects.get(pk=Social).pk
        game = Game.objects.create(title='Among Us', summary='Prueba')
        game.save()
        data = {'title': game.title, 'summary': game.summary, 'genre': genre }
        
        with open('catalogo/static/img/amongus.jpg', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/jpg')
        
        form = GameForm(data, {'image': document})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Genre.objects.create(name='Social', summary='Prueba')
        game = Game.objects.create(title='', summary='Prueba', genre=g )
        data = {'title': game.title, 'summary': game.summary, 'genre': game.genre }
        form = GameForm(data=data)
        self.assertFalse(form.is_valid())