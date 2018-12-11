import hashlib

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.utils.crypto import get_random_string


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        s_key = get_random_string(20, chars)
        k = hashlib.sha256((s_key + user.username).encode('utf-8')).hexdigest()
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.username) + k
        )


"""class TokenGenerator1(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.username)
        )
"""

account_activation_token = TokenGenerator()
#password_reset_token = TokenGenerator1()