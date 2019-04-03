# coding: utf-8

import pytest

from devto import podcast_episodes, podcast_episodes_by_username


def test_podcast_episodes(vcr):
    with vcr.use_cassette("podcast_episodes_get"):
        assert podcast_episodes()


def test_podcast_episodes_defaults_to_first_page(vcr):
    with vcr.use_cassette("podcast_episodes_get_default_page"):
        default_page = podcast_episodes()
        page_1 = podcast_episodes(page=1)
        assert default_page == page_1


def test_podcast_episodes_second_page(vcr):
    with vcr.use_cassette("podcast_episodes_get_page_2"):
        page_1 = podcast_episodes(page=1)
        page_2 = podcast_episodes(page=2)
        assert page_1 != page_2


def test_podcast_episodes_by_username(vcr):
    with vcr.use_cassette("podcast_episodes_get_by_username"):
        for podcast_episode in podcast_episodes_by_username("rubyrogues"):
            assert "rubyrogues" in podcast_episode["podcast"]["slug"]


def test_podcast_episodes_by_username_second_page(vcr):
    with vcr.use_cassette("podcast_episodes_get_by_username_page_2"):
        page_1 = podcast_episodes_by_username("rubyrogues", page=1)
        page_2 = podcast_episodes_by_username("rubyrogues", page=2)
        assert page_1 != page_2


def test_podcast_episodes_by_username_unknown_username(vcr):
    with vcr.use_cassette("podcast_episodes_get_by_username_unknown_username"):
        assert not podcast_episodes_by_username("fo1obarabo1of")


def test_podcast_episodes_by_username_nonexistent_page(vcr):
    with vcr.use_cassette("podcast_episodes_get_by_username_nonexistent_page"):
        assert not podcast_episodes_by_username("rubyrogues", page=999999999999)

