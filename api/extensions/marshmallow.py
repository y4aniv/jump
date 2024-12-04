from marshmallow import fields, validate

fields.Field.default_error_messages["required"] = "REQUIRED"
fields.Field.default_error_messages["type"] = "INVALID_TYPE"
validate.Regexp.default_message = "INVALID_FORMAT"
