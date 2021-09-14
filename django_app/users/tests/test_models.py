from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

class UserModelTests(TestCase):

    def test_user_email_must_be_unique(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='pwd')
        with self.assertRaises(IntegrityError):
            User.objects.create_user(email='normal@user.com', password='pwd')

    def test_user_has_str_method(self):
        User = get_user_model()
        email = 'normal@user.com'
        user = User.objects.create_user(email=email, password='pwd')
        self.assertEqual(str(user), email)

    def test_user_has_get_short_name_method(self):
        User = get_user_model()
        email = 'normal@user.com'
        user = User.objects.create_user(email=email, password='pwd')
        self.assertEqual(user.get_short_name(), email)

    def test_user_default_role_is_plain_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='pwd')
        self.assertEqual(user.role.value, 5)
        self.assertEqual(user.role.label, 'User')
        self.assertEqual(user.get_role_display(), 'User')

    def test_user_has_required_fields(self):
        # Will raise Atrribute Errors if fields don't exist
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='pwd')
        user.email
        user.uuid
        user.name
        user.role
        user.is_staff
        user.is_active
        user.date_joined