#!/usr/bin/env python3

import requests, re, random

travelled_path = []
r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
# r = requests.get('https://en.wikipedia.org/wiki/Dudley_Narborough')
page_content = r.content.decode()

start = re.findall(r'<h1 id="firstHeading" class="firstHeading" >(.{1,}?)<\/h1>', page_content)
travelled_path.append(start[0])

for i in range(20):
  links = re.findall(r'<a href="\/wiki\/([^"]{1,}?)" title="([^"]{1,}?)">', page_content)
  select = random.randrange(0, len(links))

  travelled_path.append(links[select][1])
  r = requests.get('https://en.wikipedia.org/wiki/%s' % links[select][0])


print(travelled_path)


