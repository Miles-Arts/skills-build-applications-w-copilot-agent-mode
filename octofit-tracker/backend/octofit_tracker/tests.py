from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        user1 = User.objects.create(username="user1", email="user1@example.com", password="password123")
        user2 = User.objects.create(username="user2", email="user2@example.com", password="password123")
        team = Team.objects.create(name="Test Team", members=[user1, user2])
        self.assertEqual(team.name, "Test Team")
        self.assertEqual(len(team.members), 2)

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration=3600)
        self.assertEqual(activity.activity_type, "Running")
        self.assertEqual(activity.duration, 3600)

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Test Workout", description="A test workout description.")
        self.assertEqual(workout.name, "Test Workout")