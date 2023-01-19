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
    # haetaan formista title,snippet ja body
    title = form['title']
    snippet = form['snippet']
    body = form['body']

    # luodaan tietokantaan collectioniin uusi JSON
    new_blog = {"title":title, "snippet":snippet, "body":body}
    # lisätään new_blog mongoon
    blogs_collection.insert_one(new_blog)

def get_blog_by_id(id):
    blog = blogs_collection.find_one({"_id":ObjectId(id)})
    return blog

def delete_blog_by_id(id):
    blogs_collection.find_one_and_delete({"_id":ObjectId(id)})

def update_blog_by_id(form, id):
    title = form['title']
    snippet = form['snippet']
    body = form['body']

    filter = {"_id":ObjectId(id)}
    update = {"$set":
             {"title":title, "snippet":snippet, "body":body}
             }

    blogs_collection.find_one_and_update(filter,update)                
    
    # tai:
    # blogs_collection.find_one_and_update(
    # {"_id":ObjectId(id)},
    #     {"$set":
    #     {"title":title, "snippet":snippet, "body":body}
    #     }
    #)

db = connect_to_mongo()
blogs_collection = db['BlogsCollection']