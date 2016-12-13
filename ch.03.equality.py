#!/usr/bin/env python
import re
import requests

INPUT_PATTERN = re.compile(r'<!--([a-zA-Z\s]+)-->')
SURROUND_BY_3_PATTERN = re.compile(r'[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}')


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    content = requests.get(url).content
    input = INPUT_PATTERN.findall(content)[0]

    print(''.join(SURROUND_BY_3_PATTERN.findall(input)))
