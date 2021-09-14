from django.contrib.auth import get_user_model
from django.test import TestCase

class UserManagerTests(TestCase):

    def test_create_user_error_as_username_doesnt_exist(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='pwd')
        with self.assertRaises(AttributeError):
            user.username

    def test_create_user_error_with_no_args(self):
        User = get_user_model()
        with self.assertRaises(TypeError):
            User.objects.create_user()

    def test_create_user_error_with_no_password_arg(self):
        User = get_user_model()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")

    def test_create_user_error_with_empty_email_string_arg(self):
        User = get_user_model()
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='pwd')

    def test_create_normal_user_success_with_correct_args(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='pwd')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # create_superuser tests
    def test_create_superuser_error_when_is_superuser_arg_False(self):
        User = get_user_model()
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='super@user.com', password='pwd', is_superuser=False)


            
    def test_create_superuser_with_correct_values_ok(self):
        User = get_user_model()
        s_user = User.objects.create_superuser(email='super@user.com', password='pwd')
        self.assertEqual(s_user.email, 'super@user.com')
        self.assertTrue(s_user.is_active)
        # Note these are different for super user, gives access to admin 
        self.assertTrue(s_user.is_staff)
        self.assertTrue(s_user.is_superuser)



