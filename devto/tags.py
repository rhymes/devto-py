# coding: utf-8

"""Dev.to API client for tags

See <https://github.com/thepracticaldev/dev.to/blob/master/app/controllers/api/v0/tags_controller.rb>
"""

from . import transport


def tags(page=1):
    """Retrieves tags."""

    return transport.get("tags", page=page)


def tags_onboarding():
    """Retrieves tags displayed in the onboarding process."""

    return transport.get("tags/onboarding")
