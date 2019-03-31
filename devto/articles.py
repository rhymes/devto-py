# coding: utf-8

"""Dev.to API client for Articles

See <https://github.com/thepracticaldev/dev.to/blob/master/app/controllers/api/v0/articles_controller.rb>
"""

from urllib.parse import urljoin

import requests

from . import exceptions
from .__version__ import __version__

BASE_URL = "https://dev.to/api/"


def articles(page=1):
    """Retrieves articles."""

    return _get_articles(page=page)


def articles_by_tag(tag, *, top=None, page=1):
    """Retrieves articles by tag."""

    return _get_articles(tag=tag, top=top, page=page)


def articles_by_username(username, *, page=1):
    """Retrieves articles by username."""

    return _get_articles(username=username, page=page)


def articles_by_organization(organization_username, *, page=1):
    """Retrieves articles by organization."""

    return articles_by_username(organization_username)


def articles_fresh():
    """Retrieves fresh articles."""

    return _get_articles(state="fresh")


def articles_rising():
    """Retrieves rising articles."""

    return _get_articles(state="rising")


def article(article_id):
    """Retrieves a single article by ID."""

    try:
        return _get("articles/%s" % article_id)
    except requests.exceptions.HTTPError as exc:
        if exc.response.status_code == requests.codes.not_found:
            raise exceptions.NotFound(str(exc)) from exc
        raise exc


def _get_articles(**params):
    return _get("articles", **params)


def _get(path, **params):
    headers = {"user-agent": "devto-py/%s" % __version__}
    response = requests.get(urljoin(BASE_URL, path), params=params, headers=headers)
    response.raise_for_status()
    return response.json()
