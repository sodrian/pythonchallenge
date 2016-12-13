#!/usr/bin/env python
import re
import zipfile
import requests

from StringIO import StringIO

NEXT_PATTERN = re.compile(r'Next nothing is ([0-9]{1,5})')


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    content = requests.get(url).content
    file_obj = StringIO(content)
    zip_file = zipfile.ZipFile(file_obj)

    comments = ''
    content = zip_file.read('90052.txt')

    while content:
        try:
            next = NEXT_PATTERN.findall(content)[0]
            next_file = '%s.txt' % next
            comments += zip_file.getinfo(next_file).comment
            content = zip_file.read(next_file)
        except IndexError:
            content = None
    print(comments)