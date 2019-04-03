# coding: utf-8
"""
All exceptions
"""


class RequestError(Exception):
    "Base exception for all errors"


class HTTPError(RequestError):
    "Base exception for all HTTP errors"


class NotFound(HTTPError):
    "Resource not found: 404"


class TimeoutError(Exception):
    "Timeout error"
