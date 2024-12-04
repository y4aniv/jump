import unittest
from http import HTTPStatus

from decorators.validate_body import validate_body
from extensions.marshmallow import fields, validate
from flask import Flask, jsonify
from marshmallow import Schema
from utils.http_response import HTTPResponse
from utils.regex import Regex


class TestSchema(Schema):
    """
    Test schema for validating the request body
    """

    email = fields.String(required=True, validate=validate.Regexp(Regex.EMAIL))
    age = fields.Integer(required=True)


class TestValidateBodyDecorator(unittest.TestCase):
    """
    Test the validate_body decorator
    """

    def setUp(self):
        """
        Create a test Flask app with a route that uses the validate_body decorator
        """
        self.app = Flask(__name__)
        self.app.testing = True

        @self.app.route("/test", methods=["POST"])
        @validate_body(TestSchema)
        def test_route():
            return jsonify({"message": "success"}), 200

    def test_valid_body(self):
        """
        Test that the route works with a valid request body
        """
        with self.app.test_client() as client:
            response = client.post("/test", json={"email": "jean@gmail.com", "age": 30})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"message": "success"})

    def test_missing_fields(self):
        """
        Test that the route returns an error when the request body is missing fields
        """
        with self.app.test_client() as client:
            response = client.post("/test", json={"age": 30})
            self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
            self.assertEqual(response.json["status"], HTTPStatus.BAD_REQUEST)
            self.assertEqual(
                response.json["message"], HTTPResponse.Messages.MISSING_FIELDS
            )
            self.assertIn("email", response.json["data"])

    def test_invalid_fields(self):
        """
        Test that the route returns an error when the request body has invalid fields
        """
        with self.app.test_client() as client:
            response = client.post("/test", json={"email": "123", "age": "thirty"})
            self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
            self.assertEqual(response.json["status"], HTTPStatus.BAD_REQUEST)
            self.assertEqual(
                response.json["message"], HTTPResponse.Messages.INVALID_FIELDS
            )
            self.assertIn("age", response.json["data"])
            self.assertIn("email", response.json["data"])


if __name__ == "__main__":
    unittest.main()
