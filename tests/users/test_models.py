from django.test import TestCase
from users.models import CustomUser


class CustomUserModelTests(TestCase):
    def test__customuser__create__can_create(self):
        """A CustomUser model can create new users"""
        user = CustomUser.objects.create(username='Alpha', password="12345", email="asdf@asdf.dk")

        self.assertEqual(user.username, 'Alpha')
        self.assertEqual(user.email, 'asdf@asdf.dk')
