a=0
b=0
while a==0 or b==0:
    Email=input("Enter Email:\n" )
    if "@" in Email: 
        Username = Email[:Email.index('@')]
        Domain =Email[Email.index('@')+1:]
        a=len(Username)
        b=len(Domain)
        c = "gmail.com" 
        d ="rediffmail.com"
        if Domain ==c or Domain == d:
            if Username and Domain: 
                print("Username: ",Username)
                print("Domain: ",Domain,"\n")
            else:
                print("Username: ?")
                print("Domain: ",Domain)
                print("please enter correct Email with username\n")
        elif Username:
            print("Username: ",Username)
            print("Domain: ?")
            print("please enter correct Email with domain!\n")
        else:
            print("invalid domain!\n")    
            
    elif "@" not in Email:
        print("Username: ",Email)
        print("Domain: ?")
        print("please enter correct Email with domain!\n")
    else :
        print("Invalid Email please enter valid Email!")
