import json
import datetime as time
now = time.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 17:
    print("Good afternoon")

elif hour > 17 and hour < 19:
    print("Good evening")
else:
    print('Good night.')
    
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
        print("Welcome  "+username)
        print("what do you want to do")
    def multy():
        print('''
                1.Enter new residents
                2.veiw  all residents
                3.Exit
                ''')
        
        c = input("chose the category you want:  ")
        if c == '1':
            def new_resident():
                b = input("pls enter new name: ")
                print("you have added "+ b)
                e = input("do you want to add another name yes(y)/no(n)")
                if e == 'y':
                    new_resident()
                elif e == 'n':
                    multy()
                    print(b)
                    file = open('person.txt','w') 
                    file.write(e) 
                    file.close()
            new_resident()
        elif c == '2':
            def show():
                file = open('person.txt','r')
                for text in file:
                    print(text)
                y = input("click e to go back to menu e: ")
                if y == 'e':
                    multy()
                else:
                    print("wrong key try again")
                    print(y)
            show()
        elif c == '3':
            print("good bye")
    multy()    
    complete = True