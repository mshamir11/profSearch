import pymongo
import json
from pymongo.collation import Collation
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["prof_search"]


mycol = mydb["prof_data"]

mylist = [{"_id": "plJC8R0AAAAJ", "Name": "Anirban Dasgupta", "Affiliation": "IIT Gandhinagar", 
              "Pic": "https://scholar.googleusercontent.com/citations?view_op=view_photo&user=plJC8R0AAAAJ&citpid=1", 
              "Homepage_url": "https://sites.google.com/site/anirbandasgupta/", 
              "Research_Interests": ['algorithms','data mining','social networks'], 
              "Google_Scholar_url": "https://scholar.google.co.in/citations?user=plJC8R0AAAAJ&hl=en", 
              "Cites_per_year": {"2004": 23, "2005": 21, "2006": 38, "2007": 117, "2008": 170, "2009": 230, "2010": 294, "2011": 358, "2012": 444, "2013": 570, "2014": 659, "2015": 716, "2016": 772, "2017": 767, "2018": 797, "2019": 710, "2020": 650, "2021": 211}, 
              "Total_Citations": 7752, "Citations_last_5_year": 3907, "hindex": 29, "hindex5y": 23, "i10index": 48, "i10index5y": 38, "Score": 0.066},
              {"_id": "jt38uQ8AAAAJ", "Name": "Manoj Gupta", "Affiliation": "IIT Gandhinagar", 
              "Pic": "https://iitgn.ac.in/media/pages/faculty/cse/manoj/3375263455-1600344525/manoj.JPG", 
              "Homepage_url": "https://www.cse.iitd.ac.in/~gmanoj/", 
              "Research_Interests": ['algorithms','Data Structures','Graph Algorithms'], 
              "Google_Scholar_url": "https://scholar.google.co.in/citations?user=jt38uQ8AAAAJ&hl=en", 
              "Cites_per_year": {"2012": 3, "2013": 9, "2014": 20, "2015": 23, "2016": 48, "2017": 52, "2018": 78, "2019": 61, "2020": 72, "2021": 37}, 
              "Total_Citations": 419, "Citations_last_5_year": 348, "hindex": 9, "hindex5y": 9, "i10index": 9, "i10index5y": 8, "Score": 0.019},
              {"_id": "U2NUj90AAAAJ", "Name": "Mayank Singh", "Affiliation": "IIT Gandhinagar", 
              "Pic": "https://scholar.googleusercontent.com/citations?view_op=view_photo&user=U2NUj90AAAAJ&citpid=1", 
              "Homepage_url": "https://mayank4490.github.io/", 
              "Research_Interests": ['NLP','data mining','Complex Networks'], 
              "Google_Scholar_url": "https://scholar.google.co.in/citations?user=U2NUj90AAAAJ&hl=en", 
              "Cites_per_year": {"2016": 4, "2017": 12, "2018": 23, "2019": 31, "2020": 38, "2021": 20}, 
              "Total_Citations": 133, "Citations_last_5_year": 130, "hindex": 6, "hindex5y": 6, "i10index": 5, "i10index5y": 5, "Score": 0.012},
              {"_id": "rFGzHlIAAAAJ", "Name": "Nipun Batra", "Affiliation": "IIT Gandhinagar", 
              "Pic": "https://scholar.googleusercontent.com/citations?view_op=view_photo&user=rFGzHlIAAAAJ&citpid=5", 
              "Homepage_url": "https://nipunbatra.github.io/", 
              "Research_Interests": ['Computational sustainability','Smart buildings','Energy Disaggregation','NILM','Air quality'], 
              "Google_Scholar_url": "https://scholar.google.co.in/citations?user=rFGzHlIAAAAJ&hl=en", 
              "Cites_per_year": {"2014": 49, "2015": 108, "2016": 127, "2017": 131, "2018": 136, "2019": 244, "2020": 241, "2021": 89}, 
              "Total_Citations": 1157, "Citations_last_5_year": 969, "hindex": 17, "hindex5y": 16, "i10index": 18, "i10index5y": 18, "Score": 0.036}]

x = mycol.insert_many(mylist)
# mycol.create_index([('Name','text')])
# mycol.create_index('Affiliation',collation=Collation(locale='en_US',strength=1))