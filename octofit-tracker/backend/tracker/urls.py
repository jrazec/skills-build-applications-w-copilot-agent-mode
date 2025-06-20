from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracker import views
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import path

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activity': '/activity/',
        'leaderboard': '/leaderboard/',
        'workouts': '/workouts/',
    })

urlpatterns = [
    path('api/', api_root, name='api-root'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('teams/', views.TeamListView.as_view(), name='team-list'),
    path('activity/', views.ActivityListView.as_view(), name='activity-list'),
    path('leaderboard/', views.LeaderboardListView.as_view(), name='leaderboard-list'),
    path('workouts/', views.WorkoutListView.as_view(), name='workout-list'),
]
