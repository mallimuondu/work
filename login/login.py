compite = False; 
user = {
"malli" : "Malli2010!",
 "nesh" : "1234",
"sharon": "sharon2008"
}
while not compite:
    username = input("username")
    passwored = input("passwored")
    if username == user and passwored == passwored:
        continue
    elif username != user:
        print("This  is not a valid username, input username again")
        continue
    elif username != user[username]:
        print("password is not valid for username,input username again!")
        continue
        
    elif passwored == user[username]:
        print("welcome username")
        
        print("thanyou for login in")
        compite = True
print("Username and Password Validated in Python")