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
            data["firstName"] = data["firstName"].strip().title()

        if isinstance(data.get("lastName"), str):
            data["lastName"] = data["lastName"].strip().title()

        if isinstance(data.get("email"), str):
            data["email"] = data["email"].strip().lower()

        return data

    firstName = fields.String(required=True, validate=validate.Regexp(Regex.FIRST_NAME))
    lastName = fields.String(required=True, validate=validate.Regexp(Regex.LAST_NAME))
    email = fields.Email(required=True, validate=validate.Regexp(Regex.EMAIL))
    password = fields.String(required=True, validate=validate.Regexp(Regex.PASSWORD))
