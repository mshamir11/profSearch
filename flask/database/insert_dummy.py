import pymongo
import json
from pymongo.collation import Collation
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["prof_search"]


mycol = mydb["inverted_index"]
prof_data = mydb['prof_data']

# f = open("./prof_data.json")
# mylist = json.load(f)

# x = mycol.insert_many(mylist)
# print(x.inserted_ids)


# prof_data.create_index([("Name","text")])


# prof_data.create_index('name',collation=Collation(locale='en_US',strength=1))
# x = prof_data.find({"Affiliation":"iit gandhinagar"}).collation(Collation(locale='en_US',strength=1)).sort([("Score",pymongo.DESCENDING)])


x = mycol.find({"_id":"risk"})

# x=prof_data.find({"$text": {"$search": "neeldhara"}})
prof_ids=set()
for item in x:
  for single_id in item['profs']:
    if single_id not in prof_ids:
      prof_ids.add(single_id)

prof_details=[]
for prof_id in prof_ids:
  # print(prof_id)
  a = prof_data.find({"_id":prof_id })
  prof_details.append(list(a)[0])

prof_details.sort(key = lambda x:x['Score'],reverse=True)


print(prof_details)

