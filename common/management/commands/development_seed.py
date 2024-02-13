from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


def test_user_seed():
    User.objects.create_superuser('test', 'test@test.com', 'test')
    User.objects.create_user('fermin', 'fermin@test.com', 'fermin')


class Command(BaseCommand):

    def handle(self, *args, **options):
        test_user_seed()
