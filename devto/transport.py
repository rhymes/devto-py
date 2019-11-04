# coding: utf-8

"""Dev.to API client transport"""

from urllib.parse import urljoin

import httpx

from . import exceptions
from .__version__ import __version__


BASE_URL = "https://dev.to/api/"


def get(path, **params):
    "Calls the HTTP REST API to retrieve resources"

    headers = {"user-agent": "devto-py/%s" % __version__}

    try:
        response = httpx.get(
            urljoin(BASE_URL, path), params=params, headers=headers, timeout=2
        )
        response.raise_for_status()
        return response.json()
    except httpx.exceptions.Timeout as exc:
        raise exceptions.TimeoutError(str(exc)) from exc
    except httpx.exceptions.HTTPError as exc:
        if exc.response.status_code == 404:
            raise exceptions.NotFound(str(exc)) from exc
        raise exceptions.HTTPError(str(exc)) from exc
    except httpx.exceptions.RequestException as exc:
        raise exceptions.RequestError(str(exc)) from exc

