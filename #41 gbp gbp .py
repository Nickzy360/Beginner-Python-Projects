
day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in day_list:
    print(x)
    x=x.upper()
test_day = input("input a day of the week from this list ")
if test_day in day_list:
    print("skibidi toilet ")

while test_day not in day_list:
    print("noooooooooooooooooooooooooooooooo")    
    test_day = input("input a day of the week from this list ")
    print(day_list)