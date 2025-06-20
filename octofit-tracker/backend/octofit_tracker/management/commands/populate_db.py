from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate octofit_db with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        client = MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]

        # Test data based on monafit tracker example
        users = [
            {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
            {"email": "bob@example.com", "name": "Bob", "password": "bobpass"},
            {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
        ]
        teams = [
            {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
            {"name": "Team Beta", "members": ["carol@example.com"]}
        ]
        activities = [
            {"user_email": "alice@example.com", "activity_type": "run", "duration": 30, "timestamp": "2025-06-20T08:00:00Z"},
            {"user_email": "bob@example.com", "activity_type": "walk", "duration": 45, "timestamp": "2025-06-20T09:00:00Z"},
            {"user_email": "carol@example.com", "activity_type": "cycle", "duration": 60, "timestamp": "2025-06-20T10:00:00Z"}
        ]
        leaderboard = [
            {"team": "Team Alpha", "score": 75},
            {"team": "Team Beta", "score": 60}
        ]
        workouts = [
            {"name": "Morning Run", "description": "A 30-minute run to start the day."},
            {"name": "Evening Walk", "description": "A relaxing 45-minute walk."}
        ]

        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
