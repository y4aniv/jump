class Regex:
    """
    A class to store regex patterns.
    """

    EMAIL = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    PASSWORD = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$"
    FIRST_NAME = LAST_NAME = r"^[a-zA-Z]{2,50}$"
