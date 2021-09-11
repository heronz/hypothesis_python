from enum import Enum


class HTTPMethodsEnum(Enum):
    """
    Enum for the possible methods for the API
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
