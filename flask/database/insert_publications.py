import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["prof_search"]


mycol = mydb["publications"]

f = open("./Publications.json")
data=json.load(f)

final_list = []

for item in data.keys():
  dic = {}
  dic['_id']=item
  try:
    if (len(data[item])>11):
      dic['publications']=data[item][:10]
  except:
    dic['publications']=data[item]

  final_list.append(dic)
  # print(final_list)
  

x = mycol.insert_many(final_list)

  
