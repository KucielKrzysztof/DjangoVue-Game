from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes
from .models import *
from .serializers import PlayerScoreSerializer
from django.shortcuts import render
from django.db.models import Max


@api_view(['POST'])
def submit_score(request):
    player_name = request.data.get('player_name')
    score = request.data.get('score')

    if player_name and score:
        PlayerScore.objects.create(player_name=player_name, score=score)
        return Response({"message": "Score submitted successfully."})
    else:
        return Response({"message": "Invalid data."}, status=400)
    
@api_view(['GET'])
def scoreboard(request):
    scores = PlayerScore.objects.values('player_name').annotate(max_score=Max('score')).order_by('-max_score')
    context = {'scores': scores}
    return render(request, 'scoreboard.html', context)
