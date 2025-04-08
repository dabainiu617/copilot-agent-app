from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        users = [
            User(_id=ObjectId(), username='john_doe', email='john@example.com', password='password123'),
            User(_id=ObjectId(), username='jane_doe', email='jane@example.com', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create test teams
        team = Team(_id=ObjectId(), name='Team Alpha')
        team.save()
        team.members.add(*users)

        # Create test activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Running', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Cycling', duration=timedelta(minutes=45)),
        ]
        Activity.objects.bulk_create(activities)

        # Create test leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=150),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create test workouts
        workouts = [
            Workout(_id=ObjectId(), name='Morning Run', description='A quick morning run to start the day'),
            Workout(_id=ObjectId(), name='Evening Cycle', description='A relaxing evening cycling session'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
