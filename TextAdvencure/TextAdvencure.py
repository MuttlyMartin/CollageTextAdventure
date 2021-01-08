import random

from time import sleep

Name = input("Enter your name adventure: ")



def Menu():

    print("Hallo! " + Name, "The fate of the jungle is in your hands!")



    print(" ___________________________________________________________ ")
    print(" |             welcome adventurer to the jungle            | ")
    print(" |                                                         | ")
    print(" |                press Space to continue                  | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Space: ")

    if choice == " ":
        StartRoom()

    else:

        #---------Invalid Input------------

        Menu()


def StartRoom():

    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                the player awakens there are             | ")
    print(" |             mounds of spoiled bodies across you         | ")
    print(" |                                                         | ")
    print(" |                       press W S A  D                    | ")
    print(" |                        to continue                      | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Direction: ")

    if choice == "w" or choice == "W":
        UpperRoom()

    elif choice == "S" or choice == "s":
        LowerRoom()

    elif choice == "A" or choice == "a":
        LeftRoom()

    elif choice == "D" or choice == "d":
        RightRoom()

    else:
        #---------Invalid Input------------
        StartRoom()

    #-------------X axis center------------------

def LeftRoom():

    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" |        a huge spider lies upside down before you        | ")
    print(" |                                                         | ")
    InpaleingChance = random.randint(1,2)
    if InpaleingChance == 1:
        print(" |           it springs its leg right into your heart,     | ")
        print(" |                   killing you straight                  | ")
        sleep(2)
        print(" |                well at least it was quick               | ")
        print(" ----------------------------------------------------------- ")
        sleep(3)
        Menu()
    else:
        print(" |            the spider missed with great envy            | ")
        sleep(2)
        print(" |       you strike it down, from its sticky ceiling       | ")
        print(" |                   killing it in one hit                 | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                       press W S A D                     | ")
    print(" |                        to continue                      | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Direction: ")

    if choice == "W" or choice == "w":
        UpperLeft()

    elif choice == "S" or choice == "s":
        LowerLeft()

    elif choice == "A" or choice == "a":
        Cliff()

    elif choice == "D" or choice == "d":
        StartRoom()

    else:
        #---------Invalid Input------------
        LeftRoom()


def RightRoom():

    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" | you enter a luscious garden, not to be miss understood  | ")
    print(" |              a HUGE snake towers over you               | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    NeckChance = random.randint(1,2)
    if NeckChance == 1:
        print(" |       its ferocious teeth, dig deep into your neck.     | ")
        print(" |        The poison digging deeper into your skin,        | ")
        print(" |                  killing you slowly                     | ")
        sleep(2)
        print(" |                 well that was painful                   | ")
        print(" ----------------------------------------------------------- ")
        sleep(3)
        Menu()
    else:
        print(" |            the snake missed with great envy             | ")
        sleep(2)
        print(" |            you strike it down, from its nest            | ")
        print(" |                   killing it in one hit                 | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Direction: ")

    if choice == "w" or choice == "W":
        UpperRight()

    elif choice == "S" or choice == "s":
        LowerRight()

    elif choice == "A" or choice == "a":
        StartRoom()

    elif choice == "D" or choice == "d":
        Cliff()

    else:
        #---------Invalid Input------------
        LeftRoom()

#-------------Y axis center------------------

def UpperRoom():

    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |               you walk on to the top room               | ")
    print(" |            to find a huge monster and so...!            | ")
    print(" |                                                         | ")
    print(" |                the monster swings and...                | ")
    DodgeChance = random.randint(1,2)
    if DodgeChance == 1:
        print(" |      you missed the chance to doge and die on impact    | ")
        print(" ----------------------------------------------------------- ")
        sleep(3)
        Menu()
    else:
        print(" |   you dodged just in time, and struck it in the head    | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                       press W S A D                     | ")
    print(" |                        to continue                      | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Direction: ")

    #print("Test")

    if choice == "W" or choice == "w":

        Cliff()

    elif choice == "S" or choice == "s":

        StartRoom()

    elif choice == "A" or choice == "a":
        UpperLeft()

    elif choice == "D" or choice == "d":
        UpperRight()

    else:
        #---------Invalid Input------------
        UpperRoom()

def LowerRoom():

    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" |              you enter to a room filled with            | ")
    print(" |                      ancient treasure                   | ")
    print(" |                                                         | ")
    print(" |        But there is a HUGE drop, spanning for miles     | ")
    FallChance = random.randint(1,2)
    if FallChance == 1:
        print(" |            you missed the jump and fall for             | ")
        print(" |              miles hitting a pile a spikes              | ")
        print(" ----------------------------------------------------------- ")
        sleep(3)
        Menu()
    else:
        print(" |    you SMACKED the side of the wall just climbing up    | ")
        sleep(2)
        print(" |                 The treasure VANISHED!                  | ")
        sleep(1)
        print(" |                  must of been a trick!                  | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |                       press W S A D                     | ")
    print(" |                        to continue                      | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Direction: ")

    if choice == "W" or choice == "w":

        StartRoom()

    elif choice == "S" or choice == "s":

        Cliff()

    elif choice == "A" or choice == "a":
        LowerLeft()

    elif choice == "D" or choice == "d":
        LowerRight()

    else:
        #---------Invalid Input------------
        LowerRoom()

    #------------Top Corners---------------------

def UpperRight():
    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    SneekChance = random.randint(1, 2)
    if SneekChance == 1:
        print(" |               you enter to find a huge HAND!            | ")
        print(" |                  you attempt to sneak by...             | ")
        sleep(1)
        print(" |          the hand twitches awake and picks you up       | ")
        print(" |     it crushes you alive at once killing you quickly    | ")
        print(" |                                                         | ")
        print(" ----------------------------------------------------------- ")
        sleep(3)
        Menu()
    else:
        print(" |     you sneak around to a safe part of the room         | ")
        print(" |        its around 2 meters away from the hand           | ")
    print(" |                                                         | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Direction: ")

    if choice == "W" or choice == "w":
        Cliff()

    elif choice == "A" or choice == "a":
        UpperRoom()

    elif choice == "D" or choice == "d":
        Cliff()

    elif choice == "S" or choice == "s":
        RightRoom()

    else:
        #---------Invalid Input------------
        LowerRoom()

def UpperLeft():
    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" |          this room was half of it missing?!?            | ")
    LeftHalfARoom = random.randint(1,2)
    if LeftHalfARoom == 1:
        print(" |                   You slipped and fell,                 | ")
        print(" |                  hitting a pile a spikes                | ")
        print(" ----------------------------------------------------------- ")
        sleep(3)
        exit(self= -1)
    else:
        print(" |                you sit stable on the ledge              | ")
        print(" |               unsure how fare it goes down              | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Direction: ")

    if choice == "W" or choice == "w":
        Cliff()

    elif choice == "A" or choice == "a":
        Cliff()

    elif choice == "D" or choice == "d":
        UpperRoom()

    elif choice == "S" or choice == "s":
        LeftRoom()

    else:
        #---------Invalid Input------------
        LowerRoom()

    #------------Lower Corner--------------------

def LowerRight():
    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" |          this room was half of it missing?!?            | ")
    HalfARoom = random.randint(1,2)
    if HalfARoom == 1:
        print(" |                   You slipped and fell,                 | ")
        print(" |                  hitting a pile a spikes                | ")
        print(" ----------------------------------------------------------- ")
        sleep(3)
        Menu()
    else:
        print(" |                you sit stable on the ledge              | ")
        print(" |               unsure how fare it goes down              | ")
    print(" |                                                         | ")
    print(" ----------------------------------------------------------- ")

    choice = input("Enter Direction: ")

    if choice == "W" or choice == "w":

        RightRoom()

    elif choice == "A" or choice == "a":

        LowerRoom()

    else:
        #---------Invalid Input------------
        LowerRoom()

def LowerLeft():
    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" |            you find a door, it drags you in             | ")
    sleep(1)
    print(" |                   almost like a dream?                  | ")
    sleep(1)
    print(" |             you find yourself in your bed?              | ")
    print(" |             that was one hell of a dream?               | ")
    print(" ----------------------------------------------------------- ")
    exit(self= -1)

#------------Areas Around--------------------

def Cliff():

    print(" ___________________________________________________________ ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" |        you fell deep into the heart of the world        | ")
    print(" |                                                         | ")
    print(" |                                                         | ")
    print(" ----------------------------------------------------------- ")
    Menu()

Menu()