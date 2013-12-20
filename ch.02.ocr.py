import re
import requests
from collections import OrderedDict


input_pattern = re.compile(
    r'<!--.*find rare characters in the mess below:.*-->.*<!--(.*)-->',
    re.DOTALL)

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
content = requests.get(url).content
input = input_pattern.findall(content)[0]

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
