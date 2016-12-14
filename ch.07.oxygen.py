#/usr/bin/env python
import re
import requests
import StringIO
from PIL import Image

URL = 'http://www.pythonchallenge.com/pc/def/oxygen.png'


if __name__ == '__main__':
    content = requests.get(URL).content
    file_obj = StringIO.StringIO(content)
    file_obj.seek(0)

    image_file = Image.open(file_obj)

    message = ''

    for i in range(1, 609, 7):
        pixel = image_file.getpixel((i, 50))
        if pixel[0] == pixel[1] == pixel[2]:
            message += chr(pixel[0])

    print(message)
    print(''.join([chr(int(ch)) for ch in re.findall('[\d]+', message)]))
