from scholarly import scholarly
import time

ids = ['K-AIPzQAAAAJ','rOum2XsAAAAJ','n8xuCVkAAAAJ','mF-F-zkAAAAJ',	'chWbG70AAAAJ', '7HJzGQYAAAAJ']


# for i in ids:
#     try:
#         f = open('resutls.txt','a')
#         author = scholarly.search_author_id(i)
#         # print(author['interests'])
#         # scholarly.pprint(author)
#         print(type(author))
#         f.write(str(author))
#         f.write(',\n')
#         f.close()
#     except:
#         continue
f = open('resutls.txt','a')
search_query = scholarly.search_author('A Min Tjoa')
author = scholarly.fill(next(search_query))
#print(author)
#f.write(author)
f.write(str([pub['bib']['title'] for pub in author['publications']]))
# print([pub['bib']['title'] for pub in author['publications']])