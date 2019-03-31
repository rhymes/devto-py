# coding: utf-8
"""
All exceptions
"""


class DevtoError(Exception):
    "Base exception for all errors"


class HTTPError(DevtoError):
    "Base exception for all HTTP errors"


class NotFound(HTTPError):
    "Resource not found: 404"
