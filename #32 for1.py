#სავარჯიშო:
#7. for
#პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ეს სიტყვა ათჯერ

#1 
def exercise_1():
    word = input("input name you gp ")
    for i in range(10):
        print(word)

#8. for
#პროგრამამ მოგვთხოვოს სიტყვის შეყვანა და რიცხვის შეყვანა, დაბეჭდოს შეყვანილი სიტყვა იმდენჯერ რა რიცხვსაც შევიყვანთ

#2    
def exercise_2():
    name = input("your name")
    number = int(input("input a number"))
    for i in range(number):
     print(name)


#9. for
#პროგრამამ შეგვაყვანინოს რიცხვი და გამოიმუშვოს რენდომ რიცხვი, ჩვენს მიერ შეყვანილი რიცხვი დაიბეჭდოს იმდენჯერ, რასაც პროგრამა გამოიმუშავებს.
   
#3
def exercise_3():
    import random   
    number = input("input a number")
    random = random.randint(1,10)
    for i in range(random):
       print(number)


#10. for
#პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ეს სიტყვა 10-ის ჩათვლით
#სტრიქონები დაინომროს

#4
def exercise_4():

    word = input("input a word ")
    for i in range(10):
        print(str(i)+".", word)


#11. ჯამი
#1. დაწერეთ პროგრამა, რომელიც დათვლის რიცხვების ჯამს 0-დან 10-მდე

#5

def exercise_5():
    number = 0
    for i in range(10):
        number = number + i
    print(number)    

#2. დაწერეთ პროგრამა, რომელიც დათვლის რიცხვების ჯამს 5-დან 12-მდე

#6

def exercise_6():
    number = 0 
    for i in range(5,12):
        number = number + i
    print(number) 

#3. დაწერეთ პროგრამა, რომელიც დათვლის რიცხვების ჯამს ერთი შეყვანილი რიცხვიდან მეორე შეყვანილ რიცხვამდე

#7

def exercise_7():
    num1 = int(input("input a number you gp sigma "))
    num2 = int(input("Input a number again sigma sigma "))
    number = 0
    for i in range(num1,num2):
        number = number + i
    print(number) 

#4. დაწერეთ პროგრამა, რომელიც დათვლის რიცხვების ჯამს შემთხვევითი რიცხვიდან (0-10), შემთხვევით რიცხვამდე (10-20)

#8

def exercise_8():
    import random
    num1 = random.randint(0,10)
    num2 = random.randint(10,20)
    number = 0
    for i in range(num1,num2):
        number = number + i
    print(number) 

#5. დაწერეთ პროგრამა, რომელიც დათვლის რიცხვების ჯამს რენდომ რიცხვიდან (0-100), რენდომ რიცხვამდე (0-100).
# გაითვალისწინეთ: შესაძლოა პირველი შემთხვევითი რიცხვი იყოს მეორეზე მეტი, ეცადეთ ამუშავოთ პროგრამა ორივე შემთხვევაში. 

#9

def exercise_9():
    import random
    summ = 0
    less = num1 = random.randint(0,100)
    more = num2 = random.randint(0,100)
    if num1 > num2:
        less = num2
        more = num1 
    for i in range(less,more):
        summ = summ + i
    print(summ)
          
exercise_9()            