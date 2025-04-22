from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Match
from .forms import MatchForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # 自分の友達を取得
    friend_ids = request.user.friends.values_list('friend__id', flat=True)

    # 自分と友達のIDをセットに（自分も含める）
    relevant_user_ids = list(friend_ids) + [request.user.id]

    # 対象プレイヤーが player1 または player2 に含まれている試合を取得
    matches = Match.objects.filter(
        Q(player1__id__in=relevant_user_ids) | Q(player2__id__in=relevant_user_ids)
    ).order_by('-date')

    return render(request, 'home.html', {'matches': matches})

@login_required
def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MatchForm()
    return render(request, 'match_form.html', {'form': form})