from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from album.models import Team, Player
from album.forms import PlayerForm

# Create your views here.
class TeamListView(ListView):
    model = Team

class PlayerListView(ListView):
    model = Player

class TeamDetailView(DetailView):
    model = Team

class PlayerDetailView(DetailView):
    model = Player

def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player-list')
    else:
        form = PlayerForm()
    return render(request= request, template_name='album/player_form.html', context={'form': form})