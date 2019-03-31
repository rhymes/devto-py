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


def _get_articles(**params):
    response = requests.get(urljoin(BASE_URL, "articles"), params=params)
    return response.json()
