import requests

#parameters
start = 'https://en.wikipedia.org/wiki/Baiyi_Ancient_Town'
end = 'https://en.wikipedia.org/wiki/Nanxiang'
list_file = 'input-list.txt'

def readList(filename):
  links = []
  with open(filename) as file:
    while (line := file.readline().rstrip()):
      links.append(line)
  return links

def findRelations(article_list):
  link_dictionary = dict()
  for link in article_list:
    related_links = set()
    r = requests.get(link)
    page_content = r.content.decode()

    for item in article_list:
      if item != link and item[24:] in page_content: related_links.add(item)

    link_dictionary[link] = related_links
  return link_dictionary

articles_list = readList(list_file)
# print(articles_list)

article_relations = findRelations(articles_list)
# print(article_relations)