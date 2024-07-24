#30 dgis taimeri romelsac titoeul dgis shignit aqvs taimeri romelic shedgeba 32 elementisgan, da misi gadatrigereba xdeba randomit romelic an archevs 0s an 1s, 
#tu udris 1s mashin klientma gp gadaigo, tu ara mashin gadadi shemdeg etapze.

import random

days = 3

while days > 0:
    parking_lot = 16
    print(days, "days.")
    workingparts = 8 # part is a 1 hours , working hours is 8. h day has 8 parts
    event = 0
    while event < workingparts:
        client = random.getrandbits(1) # if client equals 1 then client came if not then it says 0
        if client == 1:
            print("we have "+str(parking_lot)+" lots")
            demanded_lots =int(input("how many lot you need:"))
            while demanded_lots > parking_lot:
                print("your demanded lots are more than our parking lots.") 
                print("we have "+str(parking_lot)+" lots")
                demanded_lots =int(input("how many lot you need:"))                  
            parking_lot = parking_lot - demanded_lots
        else:    
            print("no orders available")
        if parking_lot == 0:
            print("we are out of parking lots")
            event = 32
        else:
            event +=1
    days -=1
    print("day "+str(days)+" off!")
    print(parking_lot, "parking lots are left!\n----------")
    #gbp