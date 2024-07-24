import random

def print_word_multiple_times1():

    number = int(input("Enter a number: "))

    word = input("Enter a word: ")

    count = 0
    while count < number:
        print(word)
        count += 1






def generate_and_print_numbers():
    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)

    print("First number:", number1)
    print("Second number:", number2)

    count = 0
    while count < number2:
        print(number1)
        count += 1





def print_hello_five_times():
    count = 1
    while count <= 5:
        print(count, ": hello")
        count += 1





def print_word_multiple_times2():
    number = random.randint(1, 10)

    word = input("Enter a word: ")

    count = 0
    while count < number:
        print(word)
        count += 1




