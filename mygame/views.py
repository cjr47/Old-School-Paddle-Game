from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ScoreForm
from .models import Score

# Create your views here.
def index(request):
    score_form = ScoreForm()
    return render(request, 'index.html', {'score_form': score_form})

def ajax_create_score(request):
    # need to know initials and score
    if request.method == "POST":
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save()
            score.save()
            data = {'status okay'}
        else:
            data = {'staus not okay'}
        return JsonResponse(data)
    else:
        return JsonResponse({'method': 'what goes here?'})
    