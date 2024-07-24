table = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
attempts = 1
for i in table:
    print(i[0],i[1],i[2])
while True:
    x = input("input x ")
    if x in ["1","2","3"]:
        x=int(x)
    else:
        print("incorrect input, please enter '1','2' or '3'")
        continue

    y = input("input y ")
    if y in ["1","2","3"]:
        y=int(y)
    else:
        print("incorrect input, please enter '1','2' or '3'")
        continue

    if table[y-1][x-1] != "-":
        print("choose other square ")
    else:
        if attempts % 2 == 1:
            table[y-1][x-1] ="X"
        else:
            table[y-1][x-1] ="O"
        attempts += 1
    
    for i in table:
        print(i[0],i[1],i[2])

    for i in table:
        if i[0]==i[1]==i[2]:
            print("WIN!")


    if table[0][0]==table[1][0]==table[2][0]=="X" or table[0][1]==table[1][1]==table[2][1] or table[0][2]==table[1][2]==table[2][2]:
        print("you win ")   
 
