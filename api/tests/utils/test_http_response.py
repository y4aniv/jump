import unittest
from http import HTTPStatus

from flask import Flask
from utils.http_response import HTTPResponse


class TestHTTPResponse(unittest.TestCase):
    """
    Test cases for HTTPResponse class.
    """

    def setUp(self):
        """
        Setup method to create a Flask app and test client.
        """
        self.app = Flask(__name__)
        self.app.testing = True
        self.client = self.app.test_client()
        self.http_response = HTTPResponse

    def test_success_response(self):
        """
        Test case to check success response.
        """
        with self.app.app_context():
            data = {"key": "value"}
            response, status = self.http_response.success(data=data)
            self.assertEqual(status, HTTPStatus.OK)
            self.assertEqual(response.json, {"status": HTTPStatus.OK, "data": data})

    def test_success_response_with_cookies(self):
        """
        Test case to check success response with cookies.
        """
        with self.app.app_context():
            data = {"key": "value"}
            cookies = [{"key": "test_cookie", "value": "test_value"}]
            response, status = self.http_response.success(data=data, cookies=cookies)
            self.assertEqual(status, HTTPStatus.OK)
            self.assertEqual(response.json, {"status": HTTPStatus.OK, "data": data})
            self.assertEqual(
                response.headers.get("Set-Cookie"), "test_cookie=test_value; Path=/"
            )

    def test_error_response(self):
        """
        Test case to check error response.
        """
        with self.app.app_context():
            data = {"error": "something went wrong"}
            response, status = self.http_response.error(data=data)
            self.assertEqual(status, HTTPStatus.INTERNAL_SERVER_ERROR)
            self.assertEqual(
                response.json,
                {
                    "status": HTTPStatus.INTERNAL_SERVER_ERROR,
                    "message": HTTPResponse.Messages.INTERNAL_SERVER_ERROR,
                    "data": data,
                },
            )

    def test_error_response_with_custom_message(self):
        """
        Test case to check error response with custom message.
        """
        with self.app.app_context():
            data = {"error": "something went wrong"}
            message = "Custom error message"
            response, status = self.http_response.error(data=data, message=message)
            self.assertEqual(status, HTTPStatus.INTERNAL_SERVER_ERROR)
            self.assertEqual(
                response.json,
                {
                    "status": HTTPStatus.INTERNAL_SERVER_ERROR,
                    "message": message,
                    "data": data,
                },
            )

    def test_error_response_with_cookies(self):
        """
        Test case to check error response with cookies.
        """
        with self.app.app_context():
            data = {"error": "something went wrong"}
            cookies = [{"key": "error_cookie", "value": "error_value"}]
            response, status = self.http_response.error(data=data, cookies=cookies)
            self.assertEqual(status, HTTPStatus.INTERNAL_SERVER_ERROR)
            self.assertEqual(
                response.json,
                {
                    "status": HTTPStatus.INTERNAL_SERVER_ERROR,
                    "message": HTTPResponse.Messages.INTERNAL_SERVER_ERROR,
                    "data": data,
                },
            )
            self.assertEqual(
                response.headers.get("Set-Cookie"), "error_cookie=error_value; Path=/"
            )


if __name__ == "__main__":
    unittest.main()
