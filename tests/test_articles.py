# coding: utf-8

from devto import articles, articles_by_tag


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
