from src.bookmarks_backup import (
    parse_href_links,
    backup_page
)

href_links = parse_href_links('seeding/seed_html.html')
backup_page(href_links)
