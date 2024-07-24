login = "nick"
password = "monster"
login1 = input("Type your username: ")
password1 = input("Type your password: ")
if login == login1 and password == password1:
        print("You are now logged in your account. ")
elif login == login1 or password == password1:
    print("Either the username or password is incorrect, try again.")
else:  
      print("you are a hacker.")    
    

