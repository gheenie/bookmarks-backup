from pywebcopy import save_webpage

from src.href_parser import HrefParser


def parse_href_links(exported_bookmarks):
    """
    Read from an exported bookmarks HTML file and search for href URLs
    """

    with open(exported_bookmarks, 'r') as file:
        all_text = file.read()

        parser = HrefParser()
        parser.feed(all_text)

        return parser.get_href_links()


def save_to_file(href_links, saved_hrefs):
    """
    Save parsed hrefs to a file
    """

    hrefs_with_newlines = map(lambda x: x + '\n', href_links)

    with open(saved_hrefs, 'w') as file:
        file.writelines(hrefs_with_newlines)


def backup_page(href_links):
    """
    Download pages in full from the given URLs
    """

    download_folder = 'data/'

    for i, url in enumerate(href_links):
        save_webpage(
            url,
            download_folder,
            project_name=str(i),
            bypass_robots=True,
            open_in_browser=False
        )

        # Logging
        print(i, url)
