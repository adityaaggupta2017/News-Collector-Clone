#aditya gupta-2022031
#sahil gupta -2022430

#https://newsapi.org/v2/everything?q=Narendra Modi&from=2023-01-12&sortBy=publishedAt&apiKey=872858c53fc4461287c493877c70cddc
#students who worked toegether together-Sahil Gupta and Aditya Gupta
import requests
import json 
import webbrowser
import os 

def ifnull(var, val):
  if var is None:
    return val
  elif var=="":
    return val
  
  return var


def api_call_request(type,q,from_date,sortBy,api_key):
    api_link="https://newsapi.org/v2/"
    api_call_response=api_link+type+"?q="+q+"&from"+from_date+"&sortBy"+sortBy+"&apiKey="+api_key
    return api_call_response


#type="everything"
#q="Football"
#from_date="2022-12-18"
#sortBy="publishedAt"

type=input("Select Option for Search(top-headlines/everything): ") # can be top headlines or everything   
q=input("Keyword: ")
from_date=input("From Date(YYYY-MM-DD): ")# of the form YYYY-MM-DD
sortBy=input("Select sort Option(popularity/publishedAt):") # popularity or publishedAt

#api_key="872858c53fc4461287c493877c70cddc" #- Adu
api_key="7cd2e3475cb44420896e182451ea1673"  #-Sahi

#status=requests.get(api_call_request(type,q,from_date,sortBy,api_key))
resp = requests.get(api_call_request(type,q,from_date,sortBy,api_key))
if resp.status_code==200:
    API_Response=resp.json()
    
    F1=open(r"F1\Aditya\bonusproject\Filtered_NewsUpdates.html","w")
    FileData="<table border=2>\n"
    FileData= FileData + "<tr><th>Author</th><th>Title</th><th>description</th><th>url</th><th>urlToImage</th><th>publishedAt</th></tr>\n"
    
    T_Count=min(20, len(API_Response["articles"]))
    for i in range(0,T_Count):
      FileData= FileData + "<tr><td>" + ifnull(API_Response["articles"][i]["author"],"NA") + "</td><td>" + ifnull(API_Response["articles"][i]["title"],"NA") + "</td><td>" + ifnull(API_Response["articles"][i]["description"],"NA") + "</td><td>" + ifnull(API_Response["articles"][i]["url"],"NA") + "</td><td><img height='200' width='200' src='" + ifnull(API_Response["articles"][i]["urlToImage"],"NA") + "'></td><td>" + ifnull(API_Response["articles"][i]["publishedAt"],"NA") + "</td></tr>\n"
   

       
    FileData= FileData + "</table>"
    
    #print(FileData)
    
    F1.write(str(FileData.replace("\u200b","")))

else:
    print("the news for this does not exist")
#def title_selector(resp,title):
    #if 
webbrowser.open('file://' + os.path.realpath(r"F1\Aditya\bonusproject\Filtered_NewsUpdates.html"))
    


    
    #aditya gupta-2022031
#sahil gupta -2022430

#https://newsapi.org/v2/everything?q=Narendra Modi&from=2023-01-12&sortBy=publishedAt&apiKey=872858c53fc4461287c493877c70cddc
#students who worked toegether together-Sahil Gupta and Aditya Gupta
import requests
import json 
import webbrowser
import os 

def ifnull(var, val):
  if var is None:
    return val
  elif var=="":
    return val
  
  return var


def api_call_request(type,q,from_date,sortBy,api_key):
    api_link="https://newsapi.org/v2/"
    api_call_response=api_link+type+"?q="+q+"&from"+from_date+"&sortBy"+sortBy+"&apiKey="+api_key
    return api_call_response


#type="everything"
#q="Football"
#from_date="2022-12-18"
#sortBy="publishedAt"

type=input("Select Option for Search(top-headlines/everything): ") # can be top headlines or everything   
q=input("Keyword: ")
from_date=input("From Date(YYYY-MM-DD): ")# of the form YYYY-MM-DD
sortBy=input("Select sort Option(popularity/publishedAt):") # popularity or publishedAt

#api_key="872858c53fc4461287c493877c70cddc" #- Adu
api_key="7cd2e3475cb44420896e182451ea1673"  #-Sahi

#status=requests.get(api_call_request(type,q,from_date,sortBy,api_key))
resp = requests.get(api_call_request(type,q,from_date,sortBy,api_key))
if resp.status_code==200:
    API_Response=resp.json()
    
    F1=open(r"F1\Aditya\bonusproject\Filtered_NewsUpdates.html","w")
    FileData="<table border=2>\n"
    FileData= FileData + "<tr><th>Author</th><th>Title</th><th>description</th><th>url</th><th>urlToImage</th><th>publishedAt</th></tr>\n"
    
    T_Count=min(20, len(API_Response["articles"]))
    for i in range(0,T_Count):
      FileData= FileData + "<tr><td>" + ifnull(API_Response["articles"][i]["author"],"NA") + "</td><td>" + ifnull(API_Response["articles"][i]["title"],"NA") + "</td><td>" + ifnull(API_Response["articles"][i]["description"],"NA") + "</td><td>" + ifnull(API_Response["articles"][i]["url"],"NA") + "</td><td><img height='200' width='200' src='" + ifnull(API_Response["articles"][i]["urlToImage"],"NA") + "'></td><td>" + ifnull(API_Response["articles"][i]["publishedAt"],"NA") + "</td></tr>\n"
   

       
    FileData= FileData + "</table>"
    
    #print(FileData)
    
    F1.write(str(FileData.replace("\u200b","")))

else:
    print("the news for this does not exist")
#def title_selector(resp,title):
    #if 
webbrowser.open('file://' + os.path.realpath(r"F1\Aditya\bonusproject\Filtered_NewsUpdates.html"))
    


    
    