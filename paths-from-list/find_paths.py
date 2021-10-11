# import from list

links = []
with open('input-list.txt') as file:
  while (line := file.readline().rstrip()):
    links.append(line)

print(links)