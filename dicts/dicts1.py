def code():
    database = {}
    schema = dict(fName = "firstName",hName = "houseNuber")
    print(fname)
    print(hName)
    for key,value in schema.items():
        database[key] = input("pls enter your {}".format(value))
        print(database)
        a = input("do you want to continue Yes(y) or no(n)")
        if a == "y":
            code()    
        else:
            print("pls wait i am uppdating my system")
code()    
