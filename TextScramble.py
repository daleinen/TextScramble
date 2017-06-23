#-----------------------------------------------------
# a program that takes a string and randomly evolves into that text

import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

target = input("\n\nEnter your target text: ")
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
completed = False
generation = 0
print()

while completed == False:

    print(attemptThis)

    attemptNext = ''
    completed = True

    for i in range(len(target)):

        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
            
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.05)

time.sleep(0.5)
print("\nTarget matched! That took " + str(generation) + " generation(s)\n")
