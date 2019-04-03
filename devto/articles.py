# coding: utf-8

"""Dev.to API client for articles

See <https://github.com/thepracticaldev/dev.to/blob/master/app/controllers/api/v0/articles_controller.rb>
"""

from . import transport


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

    return transport.get("articles/%s" % article_id)


def _get_articles(**params):
    return transport.get("articles", **params)
