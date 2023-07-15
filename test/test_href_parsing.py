from src.bookmarks_backup import parse_href_links


def test_href_links_are_extracted():
    assert parse_href_links('seeding/seed_html.html') == 1
