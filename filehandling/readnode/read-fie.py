import json
def read():
    
        
    file = open('person.txt','r') 
    for alla in file: 
        print(alla)
read()

def write():
    aha = {}
    schema = dict(Firstname='first name')
    for keys,value in schema.items():
        aha[keys] = input("your {}".format(value))
        print(aha)
        with open('person.txt')as f:
            data = json.load(f)
        data.update(aha)
        with open('person.txt', 'w') as f:
            json.dump(data,f)
write()
