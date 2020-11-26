from django.contrib import admin

# Register your models here.
from . models import Game, Genre

admin.site.register(Game)
admin.site.register(Genre)
