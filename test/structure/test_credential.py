import unittest
import copy

from src.structure.auxiliar.credential import Credential

test_credential = Credential("user_test", "user_pwd")


class TestCredentialCheck(unittest.TestCase):
    def test_input_credential_not_valid(self):
        self.assertEqual(
            test_credential.check_correct_credentials("incorrect", "user_pwd"),
            False
        )
        self.assertEqual(
            test_credential.check_correct_credentials("user_test", "incorrect"),
            False
        )
        self.assertEqual(
            test_credential.check_correct_credentials("incorrect", "incorrect"),
            False
        )

    def test_input_credential_valid(self):
        self.assertEqual(
            test_credential.check_correct_credentials("user_test", "user_pwd"),
            True
        )
