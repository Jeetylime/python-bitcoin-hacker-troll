import random
import time
r2 = random.randint(1, 55)
r1 = random.randint(0, 100)
d1 = input("COMMENCE BITCOIN TRANSFER Y OR N: ")
if d1 == 'Y':
    print("Commencing Bitcoin Transfer")
    time.sleep(2)
    print("10% COMPLETED")
    time.sleep(2)
    print("20% COMPLETED")
    time.sleep(2)
    print("30% COMPLETED")
    time.sleep(2)
    print("40% COMPLETED")
    time.sleep(2)
    print("50% COMPLETED")
    time.sleep(2)
    print("60% COMPLETED")
    time.sleep(2)
    print("63% COMPLETED")
    time.sleep(2)
    print("67% COMPLETED")
    time.sleep(2)
    print("75% COMPLETED")
    time.sleep(2)
    d1 = input ("TRANSFER TAKING LONGER THAN EXPECTED ABORT OR CONTINUE:")
    if d1 == "CONTINUE":
        time.sleep(2)
        print("78% COMPLETED")
        time.sleep(2)
        print("84% COMPLETED")
        time.sleep(2)
        print("93% COMPLETED")
        time.sleep(2)
        print("98% COMPLETED")
    if 45 > r1:
        time.sleep(2)
        print ("100% COMPLETED")
        time.sleep(0.5)
        print ("TRANSFER SUCCESSFUL")
        time.sleep(2)
        print(f"{r2} BITCOIN ADDED TO BITCOIN WALLET (3232324yui2432y4342i)")
    if 55 < r1:
        time.sleep(2)
        print ("TRANSFER FAILED (THE COPS ARE ON THERE WAY)")
    if d1 == "ABORT":
        time.sleep(2)
        print("TRANSFER ABORTED")
        time.sleep(2)
        print("CURRENT WALLET BALANCE: 0.34 BITCOIN")
        time.sleep(0.75)
        print("HOW ELSE MAY I HELP YOU TODAY")

if d1 == "N":
    time.sleep(2)
    print("TRANSFER ABORTED")
    time.sleep(2)
    print("CURRENT WALLET BALANCE: 0.34 BITCOIN")
    time.sleep(0.75)
    print("HOW ELSE MAY I HELP YOU TODAY")
    time.sleep(10)
    d1 = input ("WOULD YOU LIKE TO POWER DOWN Y OR N")
    if d1 == "Y":
        time.sleep(0.5)
        print("POWERING OFF GOOD BYE")
    if d1 == "N":
        d1 = input("WHAT CAN I HELP YOU WITH TODAY")
        if d1 == POWER_OFF:
            print("POWERING OFF GOOD BYE")
