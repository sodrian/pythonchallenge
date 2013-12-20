import re
import requests


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
body_pattern = re.compile(r'and the next nothing is ([0-9]{3,5})')

for i in range(400-84):
    r = requests.get(url)
    next = body_pattern.findall(r.content)[0]
    url = url.split('=')[0] + '=' + next
    print(i, url)