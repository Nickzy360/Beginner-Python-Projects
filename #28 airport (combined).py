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

    days = 3

    while days > 0:
        parking_lot = 16
        print(days, "days.")
        workingparts = 8  # part is a 1 hour, working hours is 8. One day has 8 parts
        event = 0
        while event < workingparts:
            client = random.getrandbits(1)  # if client equals 1 then client came if not then it says 0
            if client == 1:
                print("We have " + str(parking_lot) + " lots")
                demanded_lots = int(input("How many lots do you need: "))
                while demanded_lots > parking_lot:
                    print("Your demanded lots are more than our parking lots.")
                    print("We have " + str(parking_lot) + " lots")
                    demanded_lots = int(input("How many lots do you need: "))                  
                parking_lot = parking_lot - demanded_lots
            else:    
                print("No orders available")
            if parking_lot == 0:
                print("We are out of parking lots")
main()
