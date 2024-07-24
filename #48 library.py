# gen ID like LIB00023 where first section "LIB" last 5 chars is number in five chars
import random
reg_users = {"LIB00201":['Dexter', 'Morgan', '995574054565', '01/11/2009', '1900549403930', 'yes']}

last_id = 200
id_string = "LIB"
menu_items = {"1": "add user", "2": "find user", "x": "exit"}

book_names = ""





genre = {"001":"Mystery", 
        "002":"Thriller", 
        "003":"Romance", 
        "004":"Science Fiction",
        "005":"Fantasy",
        "006":"Historical Fiction",
        "007":"Horror", 
        "008":"Crime",
        "009":"Adventure",
        "010":"Biography"}

publisher = {"001": "Penguin Books",
            "002": "HarperCollins",
            "003": "Random House",
            "004": "Tor Books",
            "005": "Bloomsbury",
            "006": "Simon & Schuster",
            "007": "Hachette Book Group",
            "008": "Macmillan Publishers",
            "009": "Scholastic Corporation",
            "010": "Oxford University Press"}

year = [2009, 20011, 1999, 2001, 2004, 1985, 2015, 2012, 1992, 1970]

authors = {"001": "Zafón Ruiz Carlos",
    "002": "Orwell George",
    "003": "Austen Jnae",
    "004": "Lee Harper",
    "005": "Fitzgerald Scott F.",
    "006": "Rowling J.K.",
    "007": "Salinger J.D.",
    "008": "Tolkien J.R.R.",
    "009": "Lindsay Jeff",
    "010": "Huxley Aldous"}


def gen_id():
    global last_id
    if last_id == 99999:
        return None
    else:
        new_id = id_string + f"{last_id + 1:0>{5}}"
        last_id += 1
        return new_id

def menu_list():
    for key, value in menu_items.items():
        print(f"{key}) {value}")

def collect_info():
    name = input("What is your name: ")
    surname = input("What is your surname: ")
    phone_number = input("What is your phone number: ")
    birthday = input("Input your birthday in DD/MM/YR: ")
    piradi_nomeri = input("Input your P/N: ")
    paid_membership = input('''Do you want to get the paid membership? 
    If "yes" - you will be able to bring the book with you, outside the library
    If "no" - you can only read the book in the library. Yes or no: ''').lower()
    user_info = [name, surname, phone_number, birthday, piradi_nomeri, paid_membership]
    return user_info

def find_user():
    user_id = input("Enter the user ID to find: ")
    if user_id in reg_users:
        print(f"User found: {reg_users[user_id]}")
    else:
        print("User not found")

# while True:
#     menu_list()
#     menu_elem = input("Enter menu item: ")
#     if menu_elem.lower() == "x":
#         break
#     elif menu_elem == "1":
#         lib_id = gen_id()
#         user_info = collect_info()
#         reg_users.setdefault(lib_id, user_info)
#     elif menu_elem == "2":
#         find_user()
#     for key, value in reg_users.items():
#         print(key, value)



print(list(genre.keys()))
def generate_book():
    id_start = "LIBZ"    
    # genre_id = random.choice(list(genre.keys()))
    for i in list(genre.keys()):
        genre_id = i
        for j in range(0,10):
            publisher_id = random.choice(list(publisher.keys()))
            year_id = random.choice(year)
            authors_id = random.choice(list(authors.keys()))
            print(f"{id_start}.{genre_id}.{publisher_id}.{year_id}.{authors_id}")
generate_book()