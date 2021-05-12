import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["prof_search"]


mycol = mydb["summary"]

f = open("./Summary.json")
data=json.load(f)

final_list = []

for item in data.keys():
  dic ={}
  dic['_id']=item
  dic['summary']=data[item]
  final_list.append(dic)
  
x = mycol.insert_many(final_list)

  
