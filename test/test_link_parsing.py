from src.bookmarks_backup import parse_html_links


def test_html_links_are_extracted():
    with open('seeding/seed_html.html', 'r') as file:
        all_text = file.read()
        print(all_text)
        assert 0 == 1
