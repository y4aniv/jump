from http import HTTPStatus
from typing import Any, Dict, List

from flask import jsonify


class HTTPResponse:
    """
    A class to create HTTP responses.
    """

    class Messages:
        """
        A class to store the error messages.
        """

        INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"

    def success(
        data: Dict[str, Any] = {},
        status: int = HTTPStatus.OK,
        cookies: List[Dict[str, Any]] = [],
    ):
        """
        Create a successful response.

        :param data: The data to be returned.
        :param status: The HTTP status code.
        :param cookies: The cookies to be set.

        :return: The response.
        """
        response = jsonify({"status": status, "data": data})

        for cookie in cookies:
            response.set_cookie(**cookie)

        return response, status

    def error(
        data: Dict[str, Any] = {},
        message: str = Messages.INTERNAL_SERVER_ERROR,
        status: int = HTTPStatus.INTERNAL_SERVER_ERROR,
        cookies: List[Dict[str, Any]] = [],
    ):
        """
        Create an error response.

        :param data: The data to be returned.
        :param message: The error message.
        :param status: The HTTP status code.
        :param cookies: The cookies to be set.

        :return: The response.
        """
        response = jsonify({"status": status, "message": message, "data": data})

        for cookie in cookies:
            response.set_cookie(**cookie)

        return response, status
