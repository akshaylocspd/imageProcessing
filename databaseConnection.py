# learn how to connect mongodb with python 
# Error: connect ECONNREFUSED if you are getting this error  in mongo db compass
# then press win+r 
# then write services.msc
# then press enter and find mongodbsomething.exe
# then start that file ,finish.
# step 1 pip install pymongo
import pymongo
import datetime
import json
# <input type="hidden" id="TokenID" name="TokenID" value="3487">
        
from bson.objectid import ObjectId
from bson import json_util
client =pymongo.MongoClient('mongodb+srv://mongodb:mongodb9881@cluster0.ziqqgag.mongodb.net/?retryWrites=true&w=majority')# database uri
# mongodb://localhost:27017
db = client['urlShortDB'] # database name
collection =db['products']# collection name

def insertSingleRecord(data):
    post_id = collection.insert_one(data).inserted_id
    print(post_id)
    return post_id
def parse_json(data):
    return json.loads(json_util.dumps(data))
def insertMultipleRecords():
    new_posts = [{"author": "Mike",
                "text": "Another post!",
                "tags": ["bulk", "insert"],
                "date": datetime.datetime(2009, 11, 12, 11, 14)},
                {"author": "Eliot",
                "title": "MongoDB is fun",
                "text": "and pretty easy too!",
                "date": datetime.datetime(2009, 11, 10, 10, 45)}]
    post_id = collection.insert_many(new_posts)
    print(post_id.inserted_ids)
def getSingleDataFromDataBase(id):
    for data in collection.find({'_id': ObjectId(id)}):
        return data
def getAllDataFromDataBase():
     for data in collection.find():
        print(data)
# print( getSingleDataFromDataBase('asd'))
def deleteData(id):
    collection.delete_one({'_id': ObjectId(id)})
# deleteData('63cbd5167110183773efd808')
def update(oldDict,newDict):
    myquery = oldDict#{'name':'vivo phone'}
    newvalues = { "$set": newDict }
    collection.update_one(myquery, newvalues)
def updateArray(oldDict,newDict):
    myquery = oldDict#{'name':'vivo phone'}
    newvalues = { "$push": newDict }
    collection.update_one(myquery, newvalues)
def countMatches(id,value):
    a=collection.count_documents({ '_id': ObjectId(id),
    'AllTokenId': { '$in': [value] },
    })
    return a
def countValueMatch(value):
    a=collection.count_documents({
    'urlKey': { '$in': [value] }
    })
    return a
def getDataFromUniqueValueFromDataBase(key,value):
    for data in collection.find({key: value}):
        return data
    # for data in collection.find({'email': email}):
    #     return data
