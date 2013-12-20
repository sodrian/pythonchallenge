import pickle
import requests


url = 'http://www.pythonchallenge.com/pc/def/banner.p'
content = requests.get(url).content
structure = pickle.loads(content)

for raw in structure:
    out = ''
    for el in raw:
        out += el[0] * el[1]
    print(out)