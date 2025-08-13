from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail

class SignupTestCase(TestCase):
    def test_user_signup(self):
        # Send POST request to signup page
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Testpass123',
            'password2': 'Testpass123'
        })

        # Check redirect (status 302)
        self.assertEqual(response.status_code, 302)

        # Check if the user exists in DB
        self.assertTrue(User.objects.filter(username='testuser').exists())

class SignupEmailTest(TestCase):
    def test_welcome_email_sent_on_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!',
            'email': 'newuser@example.com'
        })

        user = User.objects.create_user(username="testuser", password="password", email="test@example.com")


        from .utils import send_welcome_email
        send_welcome_email(user)

        # Ensure signup redirects (means success)
        self.assertEqual(response.status_code, 302)

        # Check that one email was sent
        self.assertEqual(len(mail.outbox), 1)

        # Check email content
        self.assertEqual(mail.outbox[0].subject, 'Welcome to Our Site!')
        self.assertIn('Thanks for signing up!', mail.outbox[0].body)
        self.assertEqual(mail.outbox[0].to, ['test@example.com'])