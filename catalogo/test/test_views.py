from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from catalogo.models import Genre, Game

class GenreListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_genre = 13

        for genre_id in range(number_of_genre):
            Genre.objects.create(
                name=f'Social {genre_id}',
                summary=f'Prueba {genre_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/genres/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo/genre_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['genre_list']) == 10)

    def test_lists_all_genres(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('genres')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['genre_list']) == 3)

class GameListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_game = 13
        g =Genre.objects.create(name='Social', summary='Prueba')
        with open('catalogo/static/img/amongus.jpg', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/jpg')

        for game_id in range(number_of_game):
            test_game = Game.objects.create(
                title=f'Among Us {game_id}',
                summary=f'Prueba {game_id}',
                genre= g,
                image= document
            )
            
            test_game.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogo/games/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'games.html')
      
