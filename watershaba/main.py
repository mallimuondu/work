import datetime as time
now = time.datetime.now()
hour = now.hour
if hour < 12:
    greating =  "Good morning"
elif hour > 12 and hour < 17:
    greating =  "Good afternoon"

elif hour > 17 and hour < 19:
    greating =  "Good evening"
else:
    greating = 'Good night'
        
a = {
    "0-25":"low",
    "26-50":"litt",
    "51-70":"good",
    "71-100":"wet"
} 
b= input("water levle")
if b == '0-25':
    print("waterring for 30")
elif b == '26-50':
    print("i will water for 10 mins")
elif b == '51-70':
    print("the shamba is k")
elif b == '71-100':
    print("wont water for rest of day")
    
    
    print("bye")