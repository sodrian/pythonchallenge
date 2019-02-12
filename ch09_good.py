#!/usr/bin/env python
import re
import requests
from PIL import Image, ImageDraw
from requests.auth import HTTPBasicAuth
from http_auth import HTTP_USERNAME, HTTP_PASSWORD


URL = 'http://www.pythonchallenge.com/pc/return/good.html'
FIRST_INPUT_PATTERN = r'first:\s+(.+)\s+second'
SECOND_INPUT_PATTERN = r'second:\s+(.+)\s+-->'


def _raw_to_lst(raw):
    raw = raw.replace('\n', '')
    raw = raw.split(',')
    raw = [int(el) for el in raw]
    return raw


if __name__ == '__main__':
    body = requests.get(URL, auth=HTTPBasicAuth(HTTP_USERNAME, HTTP_PASSWORD)).content
    first = _raw_to_lst(re.findall(FIRST_INPUT_PATTERN, body, re.DOTALL)[0])
    second = _raw_to_lst(re.findall(SECOND_INPUT_PATTERN, body, re.DOTALL)[0])

    image = Image.new('RGB', (640,480))
    draw = ImageDraw.Draw(image)
    draw.line(first)
    draw.line(second)
    image.show()
