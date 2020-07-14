import json
def dict():
    dictionary = {}
    schema = dict(Fname = 'firstName')
    for keys,value in schema.items():
        dictionary[keys] = input("enter your {}".format(value))
        print(dictionary)
        with open('mistake.txt') as f:
            data = json.load(f)
        data.update(dictionary)
        
        with open('mistake.txt','w') as f:
            json.dump(data,f)
            
dict()
def mar():
    file = open('mistake.txt','r')
    for text in file:
        print(text)
mar( )