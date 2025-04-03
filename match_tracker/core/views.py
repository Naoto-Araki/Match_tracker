from django.shortcuts import render
from .models import Match

def home(request):
    matches = Match.objects.all().order_by('-date')
    return render(request, 'home.html', {'matches': matches})
    
# Create your views here.
