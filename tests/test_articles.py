# coding: utf-8

import pytest

from devto import (
    articles,
    articles_by_tag,
    articles_by_username,
    articles_by_organization,
    articles_fresh,
    articles_rising,
    article,
)
from devto.exceptions import NotFound


def test_articles(vcr):
    with vcr.use_cassette("articles_get"):
        assert articles()


def test_articles_first_result_keys(vcr):
    with vcr.use_cassette("articles_get"):
        article = articles()[0]
        assert {
            "canonical_url",
            "comments_count",
            "cover_image",
            "description",
            "id",
            "path",
            "positive_reactions_count",
            "published_at",
            "slug",
            "tag_list",
            "title",
            "type_of",
            "url",
            "user",
        } == article.keys()


def test_articles_defaults_to_first_page(vcr):
    with vcr.use_cassette("articles_get_default_page"):
        default_page = articles()
        page_1 = articles(page=1)
        assert default_page == page_1


def test_articles_second_page(vcr):
    with vcr.use_cassette("articles_get_page_2"):
        page_1 = articles(page=1)
        page_2 = articles(page=2)
        assert page_1 != page_2


def test_articles_by_tag(vcr):
    with vcr.use_cassette("articles_get_by_tag"):
        for article in articles_by_tag("python"):
            assert "python" in article["tag_list"]


def test_articles_by_tag_second_page(vcr):
    with vcr.use_cassette("articles_get_by_tag_page_2"):
        page_1 = articles_by_tag("python", page=1)
        page_2 = articles_by_tag("python", page=2)
        assert page_1 != page_2


def test_articles_by_tag_unknown_tag(vcr):
    with vcr.use_cassette("articles_get_by_tag_unknown_tag"):
        assert not articles_by_tag("fo1obarabo1of")


def test_articles_by_tag_nonexistent_page(vcr):
    with vcr.use_cassette("articles_get_by_tag_nonexistent_page"):
        assert not articles_by_tag("python", page=999999999999)


def test_articles_by_tag_top(vcr):
    with vcr.use_cassette("articles_get_by_tag_top"):
        assert articles_by_tag("python", top=5)


def test_articles_by_username(vcr):
    with vcr.use_cassette("articles_get_by_username"):
        for article in articles_by_username("ben"):
            assert article["user"]["username"] == "ben"


def test_articles_by_username_second_page(vcr):
    with vcr.use_cassette("articles_get_by_username_page_2"):
        page_1 = articles_by_username("ben", page=1)
        page_2 = articles_by_username("ben", page=2)
        assert page_1 != page_2


def test_articles_by_username_unknown_username(vcr):
    with vcr.use_cassette("articles_get_by_username_unknown_username"):
        assert not articles_by_username("fo1obarabo1of")


def test_articles_by_username_works_with_organization_too(vcr):
    with vcr.use_cassette("articles_get_by_username_organization"):
        for article in articles_by_username("azure"):
            assert article["organization"]["username"] == "azure"


def test_articles_by_organization(vcr):
    with vcr.use_cassette("articles_get_by_username_organization"):
        for article in articles_by_organization("azure"):
            assert article["organization"]["username"] == "azure"


def test_articles_fresh(vcr):
    with vcr.use_cassette("articles_get_fresh"):
        assert articles_fresh()


def test_articles_rising(vcr):
    with vcr.use_cassette("articles_get_rising"):
        assert articles_rising()


def test_article(vcr):
    with vcr.use_cassette("article_get_id"):
        assert article(10)


def test_article_unknown_id(vcr):
    with vcr.use_cassette("article_get_id_unknown"), pytest.raises(NotFound):
        assert article(9999999999999999999999)
