from pymongo import MongoClient
import re


def nameindb(name):
    col = initcol()
    doc = col.find({"name": name})
    for _ in doc:
        return True
    return False


def initcol():
    username = "guest"
    password = "D1CQpxQT9FblcMGj"
    url = "mongodb+srv://{}:{}@cluster0.ag9ir.mongodb.net/?retryWrites=true&w=majority"
    myclient = MongoClient(url.format(username, password))
    dbname = "persons"
    mydb = myclient[dbname]
    return mydb["persons"]


def isvalid(string):
    return re.match(r"^([A-Za-z]+\s*)+$", string)
