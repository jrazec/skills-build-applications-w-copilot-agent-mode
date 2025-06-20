
# MongoDB models (not Django ORM)
class User:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

class Activity:
    def __init__(self, user_email, activity_type, duration, timestamp):
        self.user_email = user_email
        self.activity_type = activity_type
        self.duration = duration
        self.timestamp = timestamp

class Leaderboard:
    def __init__(self, team, score):
        self.team = team
        self.score = score

class Workout:
    def __init__(self, name, description):
        self.name = name
        self.description = description
