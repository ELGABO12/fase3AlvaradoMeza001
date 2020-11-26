from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
    path('quienessomos', views.quienessomos, name="quienessomos"),
    path('store', views.store, name="store"),
    path('formulario', views.formulario, name="formulario"),
    path('confirmacion', views.confirmacion, name="confirmacion"),
    path('register/', views.register, name="register"),
    path('games/', views.games, name='games'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail'),
    path('game/<str:pk>', views.GameDetailView.as_view(), name='game-detail'),
]

urlpatterns += [
    path('genre/create/', views.genre_new,name='genre_create'),
    path('genre/<int:pk>/update/', views.genre_edit, name='genre_update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre_delete'),
    path('game/create/', views.game_new,name='game_create'),
    path('game/<str:pk>/update/', views.game_edit, name='game_update'),
    path('game/<str:pk>/delete/', views.GameDelete.as_view(), name='game_delete'),
]