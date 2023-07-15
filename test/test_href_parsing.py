"""
Tests here are for href parsing only, not the full webpage downloads.
"""

from src.bookmarks_backup import parse_href_links


def test_href_links_are_extracted():
    href_links = parse_href_links('seeding/seed_html.html')

    assert len(href_links) == 10
    assert href_links[0] == 'https://login.live.com/login.srf?wa=wsignin1.0&ct=1352362465&rver=6.1.6206.0&sa=1&ntprob=-1&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fmail.live.com%2F%3Fowa%3D1%26owasuffix%3Dowa%252f&id=64855&snsc=1&cbcxt=mail'
    assert href_links[4] == 'https://octopus.energy/tracker-demo-detail/?context=1&code=G-1R-SILVER-2017-1-J&consumption=9988&type=gas&inapp=true'
    assert href_links[9] == 'https://bht.allocate-cloud.co.uk/EmployeeOnlineHealth/BHTLIVE/Roster/TeamRoster'
