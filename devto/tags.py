# coding: utf-8

"""Dev.to API client for Podcast episodes

See <https://github.com/thepracticaldev/dev.to/blob/master/app/controllers/api/v0/tags_controller.rb>
"""

from urllib.parse import urljoin

import requests

from . import exceptions
from .__version__ import __version__

BASE_URL = "https://dev.to/api/"


def tags(page=1):
    """Retrieves tags."""

    return _get("tags", page=page)


def tags_onboarding():
    """Retrieves tags displayed in the onboarding process."""

    return _get("tags/onboarding")


def _get(path, **params):
    headers = {"user-agent": "devto-py/%s" % __version__}

    try:
        response = requests.get(
            urljoin(BASE_URL, path), params=params, headers=headers, timeout=2
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout as exc:
        raise exceptions.Timeout(str(exc)) from exc
