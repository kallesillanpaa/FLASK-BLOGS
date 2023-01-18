from pymongo import MongoClient

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

db = connect_to_mongo()