import random
password = ""
pass_length = int(input("Enter password size : "))
char_list = ("abcdefghijk")
namelength = len(char_list)
rand_number = random.randrange(0,namelength)

while pass_length > 0:
    rand_number = random.randrange(0,namelength)
    print(char_list[rand_number])
    password = password+char_list[rand_number]
    pass_length=pass_length-1
print(password)    
print("gbp")