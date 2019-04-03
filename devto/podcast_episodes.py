# coding: utf-8

"""Dev.to API client for Podcast episodes

See <https://github.com/thepracticaldev/dev.to/blob/master/app/controllers/api/v0/podcast_episodes_controller.rb>
"""

from urllib.parse import urljoin

import requests

from . import exceptions
from .__version__ import __version__

BASE_URL = "https://dev.to/api/"


def podcast_episodes(page=1):
    """Retrieves podcast episodes."""

    return _get_podcast_episodes(page=page)


def podcast_episodes_by_username(username, *, page=1):
    """Retrieves podcast episodes by username."""

    try:
        return _get_podcast_episodes(username=username, page=page)
    except requests.exceptions.HTTPError as exc:
        if exc.response.status_code == requests.codes.not_found:
            return []
        raise exc


def _get_podcast_episodes(**params):
    return _get("podcast_episodes", **params)


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
