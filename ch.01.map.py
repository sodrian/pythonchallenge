#!/usr/bin/env python
import re
import requests

INPUT_TEXT_PATTERN = re.compile(r'''<font color="#f000f0">(.*)</tr></td>''', re.DOTALL)


def shift_the_string(s):
    ret = ''
    for letter in s:
        if ord(letter) in range(97, 97+26):
            pos = (ord(letter) - 97 + 2) % 26 + 97
            letter = chr(pos)
        ret += letter
    return ret


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/map.html'
    content = requests.get(url).content
    input = INPUT_TEXT_PATTERN.findall(content)[0]
    print(input)
    print(shift_the_string(input))
    print(shift_the_string('map'))
