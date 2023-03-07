from django.test import TestCase
from django.test import Client
from .models import Person


class PersonTests(TestCase):
    def test_person_creation(self):
        """Verify that people are created correctly"""
        alan = Person(name="Alan")
        anna = Person(name="Anna")
        self.assertEqual(alan.name, 'Alan')
        self.assertEqual(anna.name, 'Anna')


class RequestTests(TestCase):
    def test_hello_request(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
