from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser
# Create your tests here.

class userTests(TestCase):
    def setUp(self):
        self.users = get_user_model().objects.create_user(
            username="Suhaib", email="suhaib_kharwash@outlook.com", password="0000"
        )

    def test_user_creation(self):
        email = self.users.email
        self.assertEquals(self.users.username.__str__(), "Suhaib")
        self.assertEquals(self.users.email.__str__(), "suhaib_kharwash@outlook.com")

    def test_duplicates(self):
        try:
            self.user = get_user_model().objects.create_user(
                username="Suhaib", email="suhaib_kharwash@outlook.com", password="0000"
            )
        except:
            print("something went wrong with registration")