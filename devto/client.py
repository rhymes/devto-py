# coding: utf-8

"""Dev.to API client

See <https://github.com/thepracticaldev/dev.to/tree/master/app/controllers/api/v0>
"""

from urllib.parse import urljoin

import requests

BASE_URL = "https://dev.to/api/"


def articles(page=1):
    """Retrieves articles."""

    return _get_articles(page=page)


def articles_by_tag(tag, *, top=None, page=1):
    """Retrieves articles by tag."""

    return _get_articles(tag=tag, top=top, page=page)


def articles_by_username(username, *, page=1):
    """Retrieves articles by username."""

    try:
        return _get_articles(username=username, page=page)
    except requests.exceptions.HTTPError as exc:
        # unknown username results in a 500 error
        if exc.response.status_code == 500:
            return []
        raise exc


def _get_articles(**params):
    response = requests.get(urljoin(BASE_URL, "articles"), params=params)
    response.raise_for_status()
    return response.json()
