from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data for users, teams, activities, leaderboard, and workouts collections.'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "password123"},
            {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "password123"},
            {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "password123"},
            {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "password123"},
            {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "password123"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"name": "Blue Team", "members": ["thundergod", "metalgeek"]},
            {"name": "Gold Team", "members": ["zerocool", "crashoverride", "sleeptoken"]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"user": "thundergod", "activity_type": "Cycling", "duration": 3600},
            {"user": "metalgeek", "activity_type": "Crossfit", "duration": 7200},
            {"user": "zerocool", "activity_type": "Running", "duration": 5400},
            {"user": "crashoverride", "activity_type": "Strength", "duration": 1800},
            {"user": "sleeptoken", "activity_type": "Swimming", "duration": 4500},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {"user": "thundergod", "score": 100},
            {"user": "metalgeek", "score": 90},
            {"user": "zerocool", "score": 95},
            {"user": "crashoverride", "score": 85},
            {"user": "sleeptoken", "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"name": "Cycling Training", "description": "Training for a road cycling event"},
            {"name": "Crossfit", "description": "Training for a crossfit competition"},
            {"name": "Running Training", "description": "Training for a marathon"},
            {"name": "Strength Training", "description": "Training for strength"},
            {"name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))