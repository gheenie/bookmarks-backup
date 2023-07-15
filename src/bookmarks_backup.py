from src.href_parser import HrefParser


def parse_href_links(file_path):
    with open(file_path, 'r') as file:
        all_text = file.read()

        parser = HrefParser()
        parser.feed(all_text)

        return parser.get_href_links()
