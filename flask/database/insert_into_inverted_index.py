import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["prof_search"]


mycol = mydb["inverted_index"]

f = open("./new_inverted_index.json")
mylist = json.load(f)


final_data =[]
for item in mylist.keys():
  temp_dic={}
  temp_dic["_id"]=item
  temp_dic['profs']=mylist[item]
 
  
  final_data.append(temp_dic)



  

print(len(final_data))

x = mycol.insert_many(final_data)
mycol.create_index([("_id", "text")])



