import time
def opening():
    print("Welcome to the game. ")
    time.sleep(1)
    r=input("Would you like to play? (yes/no)  ")
    return r
def confirm():
    print("You are walking in a forest when you hear a noise.")
    time.sleep(1)
    r2=input("What do you do? (run/investigate)  ")
    return r2
def stop():
    print("Bye")
    time.sleep(5000)
    
def jog():
    print("You begin to run and notice John Hamm is chasing you.")
    time.sleep(1)
    r3=input("What now? (run/ relax) ")
    return r3
def irelax():
    print("John Hamm approaches you, and brandishes a sharpened Emmy award.")
    time.sleep(1)
    r4=input("How will you survive? (roundhouse donkey kick/ swift punch)  ")
    return r4
def iran():
    print("John Hamm catches up.")
    time.sleep(1)
    r5=input("How will you survive? (roundhouse donkey kick/ swift punch)  ")
    return r5
def inv():
    print("You walk closer and notice John Hamm is brandising a sharpened Emmy award.")
    r6=input("How will you defeat John Hamm? (roundhouse donkey kick/ swift punch)  " )
    return r6
          
def rdk():
    print("You have beaten John Hamm. Congratulations.")
    time.sleep(500)
def sp():
    print("John Hamm catches your punch and combats it with a roundhouse donkey kick. You are defeated.")
    time.sleep(500)

a = opening()
if a=="yes":
    q=confirm()
    if q=="run":
      b = jog()
      if b =="run":
            d = iran()
            if d== "roundhouse donkey kick":
                    rdk()
            else:
                    sp()
      else:
            c = inv()
            if c== "roundhouse donkey kick":
                    rdk()
            else:
                    sp()
    else:
      q=inv()
      if q== "roundhouse donkey kick":
        rdk()
      else:
        sp()
else:
    stop()
