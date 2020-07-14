complete = False
user = {"malli" : "Malli2010", "nesh" : "1234" }
 
while not complete:
    username = input("Username: ")
    password = input("Password: ")
    if username == user and password == password:
        continue
    elif username not in user:
        print("This is not a valid username, input username again!")
        continue
    elif password != user[username]:
        
        print("Password is not valid for username.")
        continue
    elif password == user[username]:
        print("Welcome username ")
        print("Thank you for logging on. ")
        complete = True
 
print ("Username and Password Validated in Python")     