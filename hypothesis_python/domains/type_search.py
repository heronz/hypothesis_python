from enum import Enum


class TypeSearchEnum(Enum):
    """
    Enum for the types of search available
    """
    TAG = "tag"
    TEXT = "text"
    USER = "user"
    ANY = "any"
