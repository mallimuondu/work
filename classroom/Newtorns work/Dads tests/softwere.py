print("hello")
a = {
"malli" : "Malli2010!",
"nesh" : "1234",
"sharon": "sharon2008"
}
b = input("please input your username: ")
c = input("please input your pasword: ")
if b != a.keys():   
    print("no such user exists")
elif c != b.value():
    print("wrong passwored")
else:
    print("welcome")
print("are you an empoyer or employee")
malli = input("employer(a) or empoyee(b):  ")
if malli == "a":
    
    def username():
        b = input("please input your username: ")
        if b == "earlycampAdmin" or b == "aziziAdmin" or b == "twitterAdmin":
            def passwrd():
                c = input("please input your passwword:  ")
                if c == "ec12!" or c == "aa34" or c == "ta36!":
                    print("welcome back")
                elif c != "ec12" or c != "aa34" or c != "ta36":
                    print("you are not regestad")
            passwrd()
        elif b != "earlycamp" or b != "Azizi" or b != "twiter":
            malli()
    username()  
elif malli == "b":
    print("please wait we are updating the system. we will get back to you later")