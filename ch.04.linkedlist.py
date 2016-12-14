#!/usr/bin/env python
import re
import requests

BODY_PATTERN = re.compile(r'and the next nothing is ([0-9]{3,5})')
URL1 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
URL2 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
URLS = (URL1, URL2)


if __name__ == '__main__':
    for url in URLS:
        for i in range(400):
            print(i, url)
            r = requests.get(url)
            body = r.content
            try:
                next = BODY_PATTERN.findall(body)[0]
                url = url.split('=')[0] + '=' + next
            except IndexError:
                print(body)
                break