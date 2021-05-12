import pymongo
import json
from pymongo.collation import Collation
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["prof_search"]


mycol = mydb["prof_data"]

f = open("./Details_New.json")
mylist = json.load(f)


# final_data =[]
# for item in mylist.keys():

#   temp_dic=mylist[item]
#   temp_dic["_id"]=item
  
 
  
#   final_data.append(temp_dic)
  



  

# # print(len(final_data))

x = mycol.insert_many(mylist)
mycol.create_index([('Name','text')])
mycol.create_index('Affiliation',collation=Collation(locale='en_US',strength=1))


# mycol.create_index([("name", "text")])



