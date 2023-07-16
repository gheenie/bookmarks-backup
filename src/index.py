from src.bookmarks_backup import (
    parse_href_links,
    save_to_file,
    backup_page
)

href_links = parse_href_links('seeding/seed_html.html')
save_to_file(href_links, 'data/parsed_hrefs.txt')
# backup_page(href_links)
