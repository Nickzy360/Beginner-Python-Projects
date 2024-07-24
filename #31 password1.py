import random

password = ""
set1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
set2 = "1234567890"
set3 = "!@#$%^&*()_+|"
char_set = ""

while True:
    difficulty = input("Choose a password difficulty : Easy (1), Medium (2), Hard (3). ")
    if difficulty != "1" and difficulty != "2" and difficulty != "3":
        print("Incorrect option, You can only type the string 1 or 2 or 3, with each representing its difficulty" )
    else:
        if difficulty == "1":
            char_set = set1
        elif difficulty == "2":
            char_set = set1 + set2
        elif difficulty == "3":
            char_set = set1 + set2 + set3
        break     
        

print(char_set)   

while True:
    pass_length =input("Choose the password length, password length must be atleast 8 or higher than it. ")
    if not pass_length.isdigit() or int(pass_length) < 8:
        print("Error, password length must be atleast 8 or higher than it")
    else:
        pass_length = int(pass_length)
        break

char_set_length = len(char_set)



while pass_length > 0:
    password = password+char_set[random.randrange(0,char_set_length)]
    pass_length = pass_length -1

print(password)