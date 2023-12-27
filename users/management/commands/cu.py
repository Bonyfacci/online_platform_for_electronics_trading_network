from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='user@sky.pro',
            first_name='user',
            last_name='user',

            is_staff=False,
            is_superuser=False
        )

        user.set_password('user')
        user.save()
