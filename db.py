from pymongo import MongoClient
from bson.objectid import ObjectId

def connect_to_mongo():
    try:
        CONNECTION_STRING="mongodb+srv://batman:robin@cluster0.fnmyz.mongodb.net/?retryWrites=true&w=majority"
        connection = MongoClient(CONNECTION_STRING)
        print("connection OK")   
        return connection['BlogsDB'] #palautetaan database
    except Exception as e:
        print("cannot connect")
        raise e

def get_all_blogs():
    blogs_collection= db['BlogsCollection'] # asetaan, mitä collectionia käytetään
    blogs = len(list(blogs_collection.find())) #montako blogia löytyy        
    
    if blogs==0: #ei blogeja
        print("EI BLOGEJA")
        all_blogs=[{"title": "No blogs found!"}]
        return all_blogs
    else: # blogeja löytyy
        print("BLOGEJA ON")
        all_blogs = blogs_collection.find() #hakee kaikki
        return all_blogs

def save_blog(form):
    blogs_collection= db['BlogsCollection']
    # haetaan formista title,snippet ja body
    title = form['title']
    snippet = form['snippet']
    body = form['body']

    # luodaan tietokantaan collectioniin uusi JSON
    new_blog = {"title":title, "snippet":snippet, "body":body}
    # lisätään new_blog mongoon
    blogs_collection.insert_one(new_blog)

def get_blog_by_id(id):
    blogs_collection= db['BlogsCollection']
    blog = blogs_collection.find_one({"_id":ObjectId(id)})
    return blog

def delete_blog_by_id(id):
    blogs_collection= db['BlogsCollection']
    blogs_collection.find_one_and_delete({"_id":ObjectId(id)})

db = connect_to_mongo()