from django.urls import path
from .views import *

urlpatterns = [
    path('submit_score/', submit_score, name='submit_score'),
    path('scoreboard/', scoreboard, name='scoreboard'),
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
]
