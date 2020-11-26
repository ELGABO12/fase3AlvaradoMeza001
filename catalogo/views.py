from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Genre
from .forms import GameForm, GenreForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    num_games=Game.objects.all()

    return render(
        request,
        'index.html',
        context={'num_games':num_games},
    )

def games(request):
    num_games=Game.objects.all()

    return render(
        request,
        'games.html',
        context={'num_games':num_games},
    )

def noticias(request):
    return render(
        request,
        'noticias.html',
    )

def quienessomos(request):

     return render(
        request,
        'quienessomos.html',
    )

def store(request):

     return render(
        request,
        'store.html',
    )

def formulario(request):
     return render(
        request,
        'formulario.html',
    )

def confirmacion(request):
     return render(
        request,
        'confirmacion.html',
    )

def register(request):
    data = {
        "form": CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/register.html', data)


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

class GameListView(generic.ListView):
    model = Game
    template_name = 'templates/catalogo/game_list.html'
    queryset = Game.objects.all()

    paginate_by = 10
    
class GameDetailView(generic.DetailView):
    model = Game

class GenreListView(generic.ListView):
    model = Genre
    template_name = 'templates/catalogo/genre_list.html'
    queryset = Genre.objects.all()

    paginate_by = 10

class GenreDetailView(generic.DetailView):
    model = Genre   

class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy('index')

class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('index')

def genre_new(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('genre-detail', pk=post.pk)
    else:
        form = GenreForm()
        return render(request, 'catalogo/genre_form.html', {'form': form})

def genre_edit(request, pk):
    post = get_object_or_404(Genre, pk=pk)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('genre-detail', pk=post.pk)
    else:
        form = GenreForm(instance=post)
    return render(request, 'catalogo/genre_form.html', {'form': form})

def game_new(request):
    if request.method == "POST":
        form = GameForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #form.save_m2m()
            return redirect('game-detail', pk=post.pk)
    else:
        form = GameForm()
        return render(request, 'catalogo/game_form.html', {'form': form})

def game_edit(request, pk):
    post = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('game_detail', pk=post.pk)
    else:
        form = GameForm(instance=post)
    return render(request, 'catalogo/game_form.html', {'form': form})
