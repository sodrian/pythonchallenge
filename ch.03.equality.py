import re
import requests

input_pattern = re.compile(r'<!--([a-zA-Z\s]+)-->')

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
content = requests.get(url).content
input = input_pattern.findall(content)[0]

surround_by_3_pattern = re.compile(r'[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}')
print(''.join(surround_by_3_pattern.findall(input)))
