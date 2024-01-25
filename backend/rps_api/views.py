from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes
from .models import *
from .serializers import PlayerScoreSerializer
from .serializers import UserRegistrationSerializer
from .serializers import UserLoginSerializer
from django.shortcuts import render
from django.db.models import Max
from django.http import JsonResponse
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



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
    scores_list = list(scores)  # important: convert the QuerySet to a list object
    return JsonResponse(scores_list, safe=False)





class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(
                    username=serializer.validated_data['username'],
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password'],
                )
                # Tutaj możesz zapisywać dodatkowe pola jak 'terms' i 'location' w zależności od twojego modelu użytkownika

                return Response({'success': True, 'message': 'Rejestracja udana'}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'success': False, 'message': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'message': 'Registration error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            
            # Sprawdź użytkownika i hasło
            # Jeśli są poprawne, wygeneruj tokeny JWT
            # Przykładowa logika logowania
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                print(f"Attempting login for user: {serializer.validated_data['username']}")  # debug

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                return Response({'success': True, 'access_token': access_token, 'refresh_token': refresh_token,'username': user.username}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'message': 'Invalid login or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'success': False, 'message': 'Login error', 'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)
