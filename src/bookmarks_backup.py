from pywebcopy import save_webpage

from src.href_parser import HrefParser


def parse_href_links(file_path):
    """
    Read from an exported bookmarks HTML file and search for href URLs
    """

    with open(file_path, 'r') as file:
        all_text = file.read()

        parser = HrefParser()
        parser.feed(all_text)

        return parser.get_href_links()


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
