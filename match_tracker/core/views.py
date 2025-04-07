from django.shortcuts import render, redirect
from .models import Match
from .forms import MatchForm

def home(request):
    matches = Match.objects.all().order_by('-date')
    return render(request, 'home.html', {'matches': matches})
    
def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MatchForm()
    return render(request, 'match_form.html', {'form': form})