import json
daterbase = {}
def adding_name():
    schema = dict( 'firstname')
    with open ('person.txt','a') as file:
        json.dump(daterbase,file)        
        file.close()
        for keys,value in schema.items():
            daterbase[keys] = input("enter student name: ".format(value))
            
            a = input("do you want do add a nothername yes(y) no(n):")
            if a == 'y' or a == 'Y':
                adding_name()
            elif a == 'n' or a == 'N':
                print("good bye")
adding_name()

def adding_text():
    with open ('person.txt','a') as file:
        json.dump(daterbase,file)
        file.write("\n")
        file.close()
adding_text()
