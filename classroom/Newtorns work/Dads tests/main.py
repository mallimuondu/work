print("hello")
a = input("Are you are an employer or employee:  ")
if a == "employer":
    print("welcome employer")
    print("do you have a client request")   
    def yn():
        b = input("yes(y) or no(n):  ")
        if b == "y":
            def proposal():
                c = input("Have you written a proposal to the client. yes(y) or no (n):  ")
                if c == "y":
                    def code():
                        d = input("has your employee finished the work yes(y) or no(n):")
                        if d == "y":
                            def happy():
                                e = input("is client happy about the work y or n: ")
                                if e == "y":
                                    def ivoice():
                                        f = input("have you written an invoice to the client. yes(y) or no (n)")
                                        if f == "y":
                                            def payment():
                                                g = input("Has the client paid you yes(y) no(n):  ")
                                                if g == "y":
                                                    print("thakyou for doing all the steps good bye")
                                                elif g == "n":
                                                    print("Go and ask the client to pay you.")
                                                    payment()
                                            payment()        
                                        elif f =="n":
                                            print("Make sure you write an ivoice to your client")
                                            ivoice()
                                    ivoice()        
                                elif e == "n":
                                    print("please cheeck the code again for till the client is happy")
                                    happy()
                            happy()
                        elif d == "n":
                            print("Make sure the employee finished the work.")
                            code()
                    code()            
                             
                elif c == "n":
                    print("Make sure you finish the proposal")
                    proposal()
            proposal()
        elif b == "n":
            print("Make sure you get a client request")
            yn()
    yn()
elif a == "employee":
    print("welcome employee")