
import re
import json

regex = r'\b[A-Za-z.0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
 
def check(email):
 
    if(re.fullmatch(regex, email)):
        return 0
    else:
        return 1

def validate_password(password):
    if len(password) > 16 or len(password) <5:
        print("make sure password has atleast 5 and makimun of 16 letter")
    elif re.search('[0-9]',password) is None:
        print("make sure password has atleast one digit")
    elif re.search('[a-z]',password) is None:
        print("make sure password has atleast one small case alphabet")
    elif re.search('[A-Z]',password) is None:
        print("make sure password has atleast one upper case alphabet")
    else :
        print("valid password")
        return 0

 
if __name__ == '__main__':
    
    Userinput = int(input(' Enter 1 to register, 2 to Login, 3 for forget password :'))
   
    
    if Userinput == 1:
        email = input('Please enter your email id :')
        
       
        a = check(email)
        if a == 0 :
            password = input(' Please enter your password :')
            print("It's Valid Email")
            b = validate_password(password)
            if b == 0 : 
               with open('LoginData.json', 'a') as f:      
                    f.write("\n" + email + "," + password)
                    print('Credentials Saved')
            
        else:
            print("Invalid Email")
    elif Userinput == 2:
        User = input("Enter your email id :") 
        PW = input("Password:")
        with open('LoginData.json', 'r') as f: 
            readable = f.read()
            lines = readable.splitlines()
            user = list(filter(lambda l:l.split(',')[0] == User and l.split(',')[1] == PW,lines))
            if user:
                   print(user)
                   print("Login successful")
            else:
                   print("Login failed, Please register.")     
            f.close()
    elif Userinput == 3:
        User = input("Enter your email id :")
        with open('LoginData.json', 'r') as f: 
            readable = f.read()
            lines = readable.splitlines() # --> ['name,pw','name,pw','name,pw']
            user = list(filter(lambda l:l.split(',')[0] == User,lines)) 
            if user:
                   print(user)
            else:
                   print("Email id not found, please register")
            
           
           
