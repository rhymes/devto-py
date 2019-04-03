# coding: utf-8

"""Dev.to API client for Podcast episodes

See <https://github.com/thepracticaldev/dev.to/blob/master/app/controllers/api/v0/podcast_episodes_controller.rb>
"""

from . import exceptions, transport


def podcast_episodes(page=1):
    """Retrieves podcast episodes."""

    return _get_podcast_episodes(page=page)


def podcast_episodes_by_username(username, *, page=1):
    """Retrieves podcast episodes by username."""

    try:
        return _get_podcast_episodes(username=username, page=page)
    except exceptions.NotFound as exc:
        return []


def _get_podcast_episodes(**params):
    return transport.get("podcast_episodes", **params)
