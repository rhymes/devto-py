# coding: utf-8

"""Dev.to API client

See <https://github.com/thepracticaldev/dev.to/tree/master/app/controllers/api/v0>
"""

from urllib.parse import urljoin

import requests

BASE_URL = "https://dev.to/api/"


def articles(page=1):
    """Retrieves articles."""

    params = {"page": page}
    response = requests.get(urljoin(BASE_URL, "articles"), params=params)
    return response.json()


def articles_by_tag(tag, *, page=1):
    """Retrieves articles by tag."""

    params = {"page": page, "tag": tag}
    response = requests.get(urljoin(BASE_URL, "articles"), params=params)
    return response.json()
