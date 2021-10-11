#!/usr/bin/env python3

import requests, re, random

travelled_path = []
r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
# r = requests.get('https://en.wikipedia.org/wiki/That_Was_the_Week_That_Was')
page_content = r.content.decode()

start = re.findall(r'<title>(.{1,}?) - Wikipedia', page_content)
travelled_path.append(start[0])

for i in range(20):
  links = re.findall(r'<a href="\/wiki\/([^"]{1,}?)" title="([^"]{1,}?)">', page_content)
  select = random.randrange(0, len(links))
  to_click = links[select][1]

  while to_click in travelled_path or ":" in to_click:
    print(" Already clicked, selecting new link.")
    select = random.randrange(0, len(links))
    to_click = links[select][1]

  travelled_path.append(to_click)
  r = requests.get('https://en.wikipedia.org/wiki/%s' % links[select][0])

print(travelled_path)


