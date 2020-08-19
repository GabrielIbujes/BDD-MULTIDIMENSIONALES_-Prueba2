import requests
from bs4 import BeautifulSoup
# Import MongoClient from pymongo so we can connect to the database
from pymongo import MongoClient

if __name__ == '__main__':
    # Instantiate a client to our MongoDB instance
    

    #db_client = MongoClient("mongodb+srv://gabo2580:gabo2580@cluster0.l92ev.mongodb.net/test")
    db_client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
    ej2 = db_client.ej2
    ej2 = ej2.posts

    response = requests.get("https://www.librimundi.com/")
    soup = BeautifulSoup(response.content, "lxml")

    post_titles = soup.find_all("a", class_="text-concat-title")

    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title.text,
            'link'  : "https://www.librimundi.com/" + post_title['href']
        })

    for post in extracted:
        if db_client.ej2.ej2.find_one({'link': post['link']}) is None:
            print("Found a new listing at the following url: ", post['link'])
            db_client.ej2.ej2.insert(post)

            