#!/usr/bin/env python
import re
import requests
from PIL import Image, ImageDraw


URL = 'http://www.pythonchallenge.com/pc/return/good.html'
FIRST_INPUT_PATTERN = r'first:(.+)second'
SECOND_INPUT_PATTERN = r''


if __name__ == '__main__':
    body = requests.get(
        URL,
        auth=requests.auth.HTTPBasicAuth('huge', 'file')).content
    print(body)
    print(re.findall(FIRST_INPUT_PATTERN, body, re.DOTALL))


    image = Image.new('RGB', (640,480))
    draw = ImageDraw.Draw(image)
    draw.line(first)
    draw.line(second)
    image.show()
