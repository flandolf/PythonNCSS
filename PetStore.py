q1 = input("What animal would you like? ")
q2 = input("How many? ")

if int(q2) < 1:
    print("That's sad. No pet for you today.")
if int(q2) == 1:
    if q1.islower():
        print("Great, here's your " + q1 + "!")
if q1.isupper():
    print("Woah! No need to shout, you'll scare the animals!")
if int(q2) > 1 & q1.islower():
    if q1.islower():
        print("Ok! " + q2 + " " + q1 + "s" + " coming right up!")


