from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from .models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            'username': 'TestUsername',
            'first_name': 'TestFirstName',
            'last_name': 'TestLastName',
            'password1': 'TestPassword1',
            'password2': 'TestPassword1',
            'email': 'test@bk.ru',
        }
        self.url = reverse('users:register')

    def test_get_user_registration(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_post_user_registration_success(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.url, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_post_user_registration_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.url, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
