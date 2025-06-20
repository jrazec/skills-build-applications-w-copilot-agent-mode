from rest_framework import serializers

# Serializers for MongoDB collections
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    # Add more fields as needed

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.EmailField())
    # Add more fields as needed

class ActivitySerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    timestamp = serializers.DateTimeField()
    # Add more fields as needed

class LeaderboardSerializer(serializers.Serializer):
    team = serializers.CharField(max_length=100)
    score = serializers.IntegerField()
    # Add more fields as needed

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    # Add more fields as needed
