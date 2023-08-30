from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create users'

    def handle(self, *args, **kwargs):
        users_to_create = [
            {
                'username': 'user1',
                'email': 'user1@example.com',
                'password': 'password1',
                'password2': 'password1',

            },
            {
                'username': 'user2',
                'email': 'user2@example.com',
                'password': 'password2',
                'password2': 'password2',

            },
            {
                'username': 'user3',
                'email': 'user3@example.com',
                'password': 'password3',
                'password4': 'password3',

            },
        ]

        for user_data in users_to_create:
            username = user_data['username']
            email = user_data['email']
            password = user_data['password']

            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username, email, password)
                self.stdout.write(self.style.SUCCESS(f'User {username} created successfully'))
            else:
                self.stdout.write(self.style.WARNING(f'User {username} already exists'))
