import json
def malli():
    asking = input("enter student name: ")        
    with open ('person.txt','a') as file:
        print("you have entered: "+asking)
        b = input("do you want to add another person yes(y)no(n): ")
        file.write("\n")
        json.dump(asking,file)
        file.close()
        if b == 'y' or b == 'Y':
            malli()
        elif b == 'n' or b == 'N':
            print("goodbye")
        elif b != 'n' or b != 'N'or   b != 'y' or b != 'Y':
            print("you did not choose an option obove!please choose either")
            d = input("you did not choose onother above yes(y)/no(n)")
            if d == 'y':
                malli()
            elif d == 'n':
                print("bye")
            elif b != 'n' or b != 'N'or   b != 'y' or b != 'Y':
                print("you did not choose an option se")
                
malli()