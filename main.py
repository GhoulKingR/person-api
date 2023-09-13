from flask import Flask, request
from bson.objectid import ObjectId
from flask_cors import cross_origin
from dotenv import load_dotenv

from lib import initcol, isvalid


app = Flask(__name__)


@app.post("/api")
@cross_origin()
def create():
    if request.headers.get("Content-Type") != "application/json":
        return ({"message": "Content-Type not supported!"}, 400)

    namereq: str = request.json["name"].title().strip()
    name = " ".join(namereq.split())

    if not isvalid(name):
        return (
            {"message": "Invalid name. Name must only contain letters and spaces"},
            400,
        )

    col = initcol()
    person = col.insert_one({"name": name})

    return ({"id": str(person.inserted_id), "name": name}, 200)


@app.get("/api")
@cross_origin()
def all():
    col = initcol()
    result = []
    for doc in col.find():
        result.append({"id": str(doc["_id"]), "name": doc["name"]})

    return result


@app.get("/api/<userid>")
@cross_origin()
def read(userid):
    col = initcol()
    docs = col.find({"_id": ObjectId(userid)})
    for doc in docs:
        return ({"id": str(doc["_id"]), "name": doc["name"]}, 200)

    return ({"message": f"User with ID {userid} doesn't exists"}, 404)


@app.put("/api/<userid>")
@cross_origin()
def change(userid):
    if request.headers.get("Content-Type") != "application/json":
        return ({"message": "Content-Type not supported!"}, 400)

    namereq: str = request.json["name"].title().strip()
    name = " ".join(namereq.split())

    if not isvalid(name):
        return (
            {"message": "Invalid name. Name must only contain letters and spaces"},
            400,
        )

    col = initcol()
    docs = col.find({"_id": ObjectId(userid)})
    for _ in docs:
        namedoc = col.find({"name": name})
        for _ in namedoc:
            return ({"message": f'Name should be unique. "{name}" already exists'}, 400)

        col.update_one({"_id": ObjectId(userid)}, {"$set": {"name": name}})
        return {"id": userid, "name": name}

    return ({"message": f"User with ID {userid} doesn't exists"}, 404)


@app.delete("/api/<userid>")
def delete(userid):
    col = initcol()
    id = ObjectId(userid)

    docs = col.find({"_id": id})
    for doc in docs:
        col.delete_one({"_id": id})
        return ({"id": str(doc["_id"]), "name": doc["name"]}, 200)

    return ({"message": f"No user with this id: {userid}"}, 400)


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
