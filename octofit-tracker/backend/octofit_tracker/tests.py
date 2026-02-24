from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='TestTeam', description='Test Desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team.name)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'TestTeam')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='TestTeam', description='Test Desc')
        self.assertEqual(team.name, 'TestTeam')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='TestTeam', description='Test Desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team.name)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2026-02-24')
        self.assertEqual(activity.type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='TestTeam', description='Test Desc')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.points, 50)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='TestWorkout', description='Desc', suggested_for='TestTeam')
        self.assertEqual(workout.name, 'TestWorkout')
