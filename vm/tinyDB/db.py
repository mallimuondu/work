from tinydb import TinyDB,Query
db = TinyDB('db.json')
def insert():
    db.insert({"name": 'malli' , 'age':9 })
    db.insert({"name": 'nesh' , 'age':11 })
    db.insert({"name": 'sharon' , 'age':13 , 'city':'kenya '}) 
insert()
print(db.all( ))