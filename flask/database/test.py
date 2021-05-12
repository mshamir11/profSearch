import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]


mycol = mydb["customers"]
print(mydb.list_collection_names())

query = {"_id": "machine learning"}

try:
    x = mycol.find(query)
    print(x[0])

except:
    print("the query is not in our list")
