#davaleba aeroportis sadgomi: sheekitxet manqanas ramdeni xani rcheba,
# shemdgom gamotvalet 1 kvira = 50 lari, 1 dge = 10 lari, 
#dagwirdebat nashtiani da unashto gayofebis gamoyeneba. 
#shesaqmnelia 2 funqcia, priveli romelic gamotvlis yvelafers, meore romelic qvitars bewdavs




import random

def parking_price(weeks, days):
    day = 10
    week = 50

    price = (weeks * 7 * week) + (days * day) if days > 0 else (weeks * week)
    return price

def parking_spot():
    num = random.randint(1, 20)
    letter = random.choice('ABCD')
    return num, letter

def main():
    weeks = int(input("How many weeks are you leaving your car? : "))
    days = int(input("How many days are you leaving your car? : "))

    price = parking_price(weeks, days)
    num, letter = parking_spot()

    print("Parking Ticket")
    print("Price in GEL:", str(price))
    print("Park your car at:", num, letter)
main()   