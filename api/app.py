from http import HTTPStatus

from flask import Flask
from utils.http_response import HTTPResponse

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error: Exception) -> tuple:
    """
    Handle the 404 error (Not Found).

    :param error: The error.

    :return: The response.
    """
    return HTTPResponse.error(
        message=HTTPResponse.Messages.NOT_FOUND, status=HTTPStatus.NOT_FOUND
    )


@app.errorhandler(405)
def method_not_allowed(error: Exception) -> tuple:
    """
    Handle the 405 error (Method Not Allowed).

    :param error: The error.

    :return: The response.
    """
    return HTTPResponse.error(
        message=HTTPResponse.Messages.METHOD_NOT_ALLOWED,
        status=HTTPStatus.METHOD_NOT_ALLOWED,
    )


@app.errorhandler(500)
def internal_server_error(error: Exception) -> tuple:
    """
    Handle the 500 error (Internal Server Error).

    :param error: The error.

    :return: The response.
    """
    return HTTPResponse.error(
        message=HTTPResponse.Messages.INTERNAL_SERVER_ERROR,
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
    )


@app.errorhandler(415)
def unsupported_media_type(error: Exception) -> tuple:
    """
    Handle the 415 error (Unsupported Media Type).

    :param error: The error.

    :return: The response.
    """
    return HTTPResponse.error(
        message=HTTPResponse.Messages.UNSUPPORTED_MEDIA_TYPE,
        status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
    )


@app.errorhandler(401)
def unauthorized(error: Exception) -> tuple:
    """
    Handle the 401 error (Unauthorized).

    :param error: The error.

    :return: The response.
    """
    return HTTPResponse.error(
        message=HTTPResponse.Messages.UNAUTHORIZED, status=HTTPStatus.UNAUTHORIZED
    )


@app.errorhandler(403)
def forbidden(error: Exception) -> tuple:
    """
    Handle the 403 error (Forbidden).

    :param error: The error.

    :return: The response.
    """
    return HTTPResponse.error(
        message=HTTPResponse.Messages.FORBIDDEN, status=HTTPStatus.FORBIDDEN
    )


if __name__ == "__main__":
    app.run()
