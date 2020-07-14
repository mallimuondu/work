import datetime as time
 greating = "hi"
    a = {
       "name":"john",
        "housenumber":"201",
        "bill":"500ksh",
        
        "name":"pual",
        "housenumber":"202",
        "bill":"2000ksh",
        
        "name":"peter",
        "housenumber":"202",
        "bill":"2500ksh",
        
        "name":"peter",
        "housenumber":"202",
        "bill":"2000ksh",
        
        "name":"sharon",
        "housenumber":"204",
        "bill":"0ksh",
    }
def get_time():
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
     
    b = a.get('name ')
    
        
        

    