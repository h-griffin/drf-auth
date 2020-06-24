from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Fish

class FishModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Fish.objects.create(
            name = 'Name of fish',
            catcher = test_user,
            description = 'Words about the fish'
        )
        test_post.save()

    def test_tank_content(self):
        fish = Fish.objects.get(id=1)

        self.assertEqual(fish.name, 'Name of fish')
        self.assertEqual(str(fish.catcher), 'tester')
        self.assertEqual(fish.description, 'Words about the fish')
