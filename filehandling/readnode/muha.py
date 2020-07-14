import json
daterbase = {}
def adding_name():
    schema = dict(fname = 'firstname')
    for keys,value in schema.items():
        daterbase[keys] = input("enter".format(value))
        print(daterbase)
        
adding_name()
def adding_text():
    with open ('person.txt','a') as file:
        json.dump(daterbase,file)
        file.write("\n")
        file.close()
adding_text()
