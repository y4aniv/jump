from typing import Any, Dict

from extensions.marshmallow import fields, validate
from marshmallow import Schema, pre_load
from utils.regex import Regex


class AuthRegisterSchema(Schema):
    """
    Schema for validating the request body when registering a new user.
    """

    @pre_load
    def normalize_data(self, data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Normalize the data before validation.
        """
        if isinstance(data.get("firstName"), str):
            data["first_name"] = data["firstName"].strip()

        if isinstance(data.get("lastName"), str):
            data["last_name"] = data["lastName"].strip()

        if isinstance(data.get("email"), str):
            data["email"] = data["email"].strip().lower()

        return data

    first_name = fields.String(
        required=True, validate=validate.Regexp(Regex.FIRST_NAME)
    )
    last_name = fields.String(required=True, validate=validate.Regexp(Regex.LAST_NAME))
    email = fields.Email(required=True, validate=validate.Regexp(Regex.EMAIL))
    password = fields.String(required=True, validate=validate.Regexp(Regex.PASSWORD))
