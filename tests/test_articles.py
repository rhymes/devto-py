# coding: utf-8

from devto import articles


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
        articles_default_page = articles()
        articles_page_1 = articles(page=1)
        assert articles_default_page == articles_page_1


def test_articles_second_page(vcr):
    with vcr.use_cassette("articles_get_page_2"):
        articles_page_1 = articles(page=1)
        articles_page_2 = articles(page=2)
        assert articles_page_1 != articles_page_2
