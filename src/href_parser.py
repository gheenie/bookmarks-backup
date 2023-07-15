"""
A custom class overriding HTMLParser to handle fed data
"""

from html.parser import HTMLParser


class HrefParser(HTMLParser):
    href_links = []

    def get_href_links(self):
        return self.href_links

    def handle_starttag(self, tag, attrs):
        """
        Only look for <a href="" /> links
        """

        if tag == 'a' and attrs[0] == 'href':
            self.href_links.push(attrs[1])
