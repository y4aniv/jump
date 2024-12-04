import unittest

from marshmallow import ValidationError
from schemas.auth.register import AuthRegisterSchema


class TestAuthRegisterSchema(unittest.TestCase):
    """
    Test the AuthRegisterSchema.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.schema = AuthRegisterSchema()

    def test_valid_data(self):
        """
        Test valid data.
        """
        valid_data = {
            "firstName": "John",
            "lastName": "Doe",
            "email": "  jOhn.doe@exAmple.com  ",
            "password": "ValidPassword123!",
        }
        result = self.schema.load(valid_data)
        self.assertEqual(result["firstName"], "John")
        self.assertEqual(result["lastName"], "Doe")
        self.assertEqual(result["email"], "john.doe@example.com")

    def test_invalid_email(self):
        """
        Test invalid email.
        """
        invalid_data = {
            "firstName": "John",
            "lastName": "Doe",
            "email": "invalid-email",
            "password": "ValidPassword123!",
        }
        with self.assertRaises(ValidationError) as context:
            self.schema.load(invalid_data)

    def test_missing_first_name(self):
        """
        Test missing first name.
        """
        invalid_data = {
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "ValidPassword123!",
        }
        with self.assertRaises(ValidationError):
            self.schema.load(invalid_data)

    def test_missing_last_name(self):
        """
        Test missing last name.
        """
        invalid_data = {
            "firstName": "John",
            "email": "john.doe@example.com",
            "password": "ValidPassword123!",
        }
        with self.assertRaises(ValidationError):
            self.schema.load(invalid_data)

    def test_missing_email(self):
        """
        Test missing email.
        """
        invalid_data = {
            "firstName": "John",
            "lastName": "Doe",
            "password": "ValidPassword123!",
        }
        with self.assertRaises(ValidationError):
            self.schema.load(invalid_data)

    def test_missing_password(self):
        """
        Test missing password.
        """
        invalid_data = {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
        }
        with self.assertRaises(ValidationError):
            self.schema.load(invalid_data)


if __name__ == "__main__":
    unittest.main()
