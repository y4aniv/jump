from functools import wraps
from http import HTTPStatus

from extensions.marshmallow import fields
from flask import request
from marshmallow import Schema, ValidationError
from utils.http_response import HTTPResponse


def validate_body(model: Schema) -> callable:
    """
    Validate the request body using the provided marshmallow schema.

    :param model: The marshmallow schema to validate the request body against

    :return: The decorated function
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                model().load(request.json)

                return func(*args, **kwargs)
            except ValidationError as error:
                missing_fields = [
                    field
                    for field, messages in error.messages.items()
                    if fields.Field.default_error_messages["required"] in messages
                ]

                invalid_fields = [
                    field for field in error.messages if field not in missing_fields
                ]

                if missing_fields:
                    return HTTPResponse.error(
                        HTTPResponse.Messages.MISSING_FIELDS,
                        HTTPStatus.BAD_REQUEST,
                        missing_fields,
                    )

                if invalid_fields:
                    return HTTPResponse.error(
                        HTTPResponse.Messages.INVALID_FIELDS,
                        HTTPStatus.BAD_REQUEST,
                        invalid_fields,
                    )

        return wrapper

    return decorator
