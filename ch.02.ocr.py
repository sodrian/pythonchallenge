#!/usr/bin/env python
import re
import requests
from collections import OrderedDict

URL = 'http://www.pythonchallenge.com/pc/def/ocr.html'
INPUT_PATTERN = re.compile(
    r'<!--.*find rare characters in the mess below:.*-->.*<!--(.*)-->',
    re.DOTALL)


if __name__ == '__main__':
    content = requests.get(URL).content
    input = INPUT_PATTERN.findall(content)[0]

    d = OrderedDict()

    for char in input:
        if char not in d:
            d[char] = 0
        d[char] += 1

    r = ''
    for k,v in d.items():
        if v == 1:
            r += k
    print(r)
