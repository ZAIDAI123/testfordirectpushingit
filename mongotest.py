import pymongo
client = pymongo.MongoClient("mongodb+srv://root:antAi78612@cluster0.rzxexhl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudh",
    "email":"sudh@ineuron.ai",
    "surname":"kumar"
}
db1 = client['mongotest']
cell = db1['test']
cell.insert_one(d)