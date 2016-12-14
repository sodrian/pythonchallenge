#!/usr/bin/env python
import bz2
import re
import requests

URL = 'http://www.pythonchallenge.com/pc/def/integrity.html'
USERNAME_PATTERN = r"un: '(.*)'"
PASSWORD_PATTERN = r"pw: '(.*)'"


if __name__ == '__main__':
    body = requests.get(URL).content

    username = re.findall(USERNAME_PATTERN, body)[0].decode('string_escape')
    password = re.findall(PASSWORD_PATTERN, body)[0].decode('string_escape')

    print(bz2.decompress(username))
    print(bz2.decompress(password))
