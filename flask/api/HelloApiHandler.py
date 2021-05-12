from flask_restful import Api, Resource, reqparse
import pymongo
from pymongo.collation import Collation


class HelloApiHandler(Resource):

  def __init__(self):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["prof_search"]
    self.prof_data = mydb["prof_data"]
    self.inverted_index = mydb["inverted_index"]



  def get(self):
    return {
      'resultStatus': 'SUCCESS',
      'message': "Hello Api Handler"
      }


  def search_research_interests(self,query):
    
    
    x = self.inverted_index.find({"_id":query})

    
    result=[]
    prof_ids=set()
    for item in x:
      for single_id in item['profs']:
        if single_id not in prof_ids:
          prof_ids.add(single_id)
    
    prof_details=[]
    for prof_id in prof_ids:
      a = self.prof_data.find({"_id":prof_id })
      prof_details.append(list(a)[0])

    
    prof_details.sort(key = lambda x:x['Score'],reverse=True)
    
    return prof_details

  def search_professor_name(self,query):
    result = self.prof_data.find({"$text": {"$search": query}}).sort([("Score",pymongo.DESCENDING)])
    
    return list(result)

  def search_university_name(self,query):
    result = self.prof_data.find({"Affiliation":query}).collation(Collation(locale='en_US',strength=1)).sort([("Score",pymongo.DESCENDING)])
    
    return list(result)

  def post(self):
    print(self)
    parser = reqparse.RequestParser()
    print(parser)
    # parser.add_argument('type', type=str)
    parser.add_argument('message', type=str)
    parser.add_argument('query_type', type=str)


    args = parser.parse_args()

    print(args)
    # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

    # request_type = args['type']
    request_json = args['message']
    request_query_type =args['query_type']
    # ret_status, ret_msg = ReturnData(request_type, request_json)
    # currently just returning the req straight
    # ret_status = request_type
    ret_msg=[]
    if request_query_type=='research_interest':
      ret_msg = self.search_research_interests(request_json)
    
    elif request_query_type=='professor_name':
      ret_msg = self.search_professor_name(request_json)
    
    elif request_query_type=='university_name':
      ret_msg=self.search_university_name(request_json)

    
    # print(ret_msg)
    return ret_msg