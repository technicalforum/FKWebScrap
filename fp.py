import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from tabulate import tabulate
import os
import pandas as pd

os.chdir("D:/RND")

def mobile_cost(brand):
  print(brand)
  model_list=[]
  price_list=[]
  ratings_list=[]
  

  for i in range(1,10
  ):
    
   my_url  = 'https://www.flipkart.com/search?q='+brand+'%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)
   uclient = req(my_url)
   page_html = uclient.read()
   page_soup = soup(page_html,'html.parser')
   uclient.close()

   containers = page_soup.findAll("div",{"class","_1-2Iqu row"})
   


   for container in containers:
    
      model_container = container.findAll("div",{"class","_3wU53n"})
      model = model_container[0].text.strip()
      model  = model.replace(",","-" )
      model_list.append(model)
      price_container = container.findAll("div",{"class","_1vC4OE _2rQ-NK"})
      price = price_container[0].text.strip()
    #price  = model.replace(" ","|" )
      price  = price.replace(",","" )
      price  = price.replace("₹","INR" )
      price_list.append(price)
      ratings_container = container.findAll("div",{"class","hGSR34"})
      if len(ratings_container) > 0:
         ratings = ratings_container[0].text.strip()
         ratings_list.append(ratings)
      else:
        ratings='NA'
        ratings_list.append(ratings)
     #ratings = ratings_container[0].text.strip()
    #ratings  = ratings.replace(" ","|" )
      print((model+","+price+ "," + ratings +"\n"))
     #f.append("\n"+model+","+price+","+ratings)
    #f.write("\n")

  df1=pd.DataFrame(model_list,columns=['model_list'])
  df1['price_list']=price_list
  df1['ratings_list']=ratings_list

  df1.to_csv(brand+'_Mobiles.csv',index = False)
  



import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	 mobile_cost('nokia')
	 return "Done"
	 
@app.route('/api/brand', methods=['GET'])
def brand():
    if ('id' in request.args):
        brand = request.args['id']
        mobile_cost(brand)
    else:
        return "Error: No brand field provided. Please specify a brand."

    
    return "brand"
	 
@app.route('/api/samsung', methods=['GET'])
def Samsung():
     mobile_cost('Samsung') 

     return 'samsung'
	
	
app.run()
