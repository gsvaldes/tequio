from django.test import TestCase

from users.forms import TequioUserCreationForm


class TestUserCreationForm(TestCase):
    def test_form_is_valid_if_neither_password_provided(self):
        form = TequioUserCreationForm(
            data={'email': 'example@example.com', 'username': 'mrexample'}
            )
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid_if_password_mismatch(self): 
        form = TequioUserCreationForm(
            data={
                'email': 'example@example.com',
                'username': 'mrexample',
                'password1': 'abcdefghi',
                'password2': 'ihgfedcba',
                }
            )
        self.assertFalse(form.is_valid())

    def test_form_is_not_valid_if_only_one_password_provided(self): 
        form = TequioUserCreationForm(
            data={
                'email': 'example@example.com',
                'username': 'mrexample',
                'password1': 'abcdefghi',
                }
            )
        self.assertFalse(form.is_valid())
        

        



