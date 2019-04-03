# coding: utf-8

import pytest

from devto import tags, tags_onboarding


def test_tags(vcr):
    with vcr.use_cassette("tags_get"):
        assert tags()


def test_tags_defaults_to_first_page(vcr):
    with vcr.use_cassette("tags_get_default_page"):
        default_page = tags()
        page_1 = tags(page=1)
        assert default_page == page_1


def test_tags_second_page(vcr):
    with vcr.use_cassette("tags_get_page_2"):
        page_1 = tags(page=1)
        page_2 = tags(page=2)
        assert page_1 != page_2


def test_tags_nonexistent_page(vcr):
    with vcr.use_cassette("tags_get_nonexistent_page"):
        assert not tags(page=999999999999)


def test_tags_onboarding(vcr):
    with vcr.use_cassette("tags_get_onboarding"):
        assert tags_onboarding()
