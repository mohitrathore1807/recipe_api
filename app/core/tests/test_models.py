from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModels(TestCase):

    def test_user_created_using_email(self):
        '''Testing that user has been successfully created using email'''
        email = 'mohit@rathore.com'
        password = "testuser123"
        user = get_user_model().objects.create_user(
            email,
            password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalized(self):
        '''checks user email gets normalize'''
        email = 'mohitrathore@G.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_invalide_user_email(self):
        '''testing that invalid user email where nothing entered'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_creating_super_user(self):
        '''Testing creating super user'''
        user = get_user_model().objects.create_superuser(
            'mohitrathore1@g.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
