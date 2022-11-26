import pymongo

client = pymongo.MongoClient("mongodb+srv://wasim:mongodb355@cluster0.dne2x.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"wasim",
    "email":"wraza355@.ai",
    "surname":"ansari"
}
db1= client['mongotest']
coll = db1['test']
coll.insert_one(d )
