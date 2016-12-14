#!/usr/bin/env python
import pickle
import requests

URL = 'http://www.pythonchallenge.com/pc/def/banner.p'


if __name__ == '__main__':
    content = requests.get(URL).content
    structure = pickle.loads(content)

    for raw in structure:
        out = ''
        for el in raw:
            out += el[0] * el[1]
        print(out)