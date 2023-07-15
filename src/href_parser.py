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

        # Only parse the 'anchor' tag
        if tag == "a":
           # Check the list of defined attributes
           for name, value in attrs:
               # If href is defined, append it
               if name == "href":
                   self.href_links.append(value)
                   break
