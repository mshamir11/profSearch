from scholarly import scholarly
import time

ids = ['x8qCMhcAAAAJ', 'WjHjbrwAAAAJ',
 'LVfqLuoAAAAJ',
 'K-AIPzQAAAAJ',
 'rOum2XsAAAAJ',
 'n8xuCVkAAAAJ']


for i in ids:
    author = scholarly.search_author_id(i)
    print(author['interests'])
    scholarly.pprint(author)
    time.sleep(2)

"""search_query = scholarly.search_author('A Min Tjoa')
author = scholarly.fill(next(search_query))
print(author)

print([pub['bib']['title'] for pub in author['publications']])"""