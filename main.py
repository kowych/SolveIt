import time
import sys
import random


def countdown(t):
    print(x1, '+', x2)
    while t:
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print("\r{0}".format(timer), end='')
        time.sleep(1)
        t -= 1
    print('\nTime expired!')


def solving():
    for i in range(15):
        print("\/")
        i += 1

    e = input("Write here: ")

    answer = x1 + x2

    if int(e) == answer:
        print("Good job!")
    else:
        print('Wrong answer!')


t = 5
x1 = random.randrange(1, 100)
x2 = random.randrange(1, 100)

print('You will have 5 seconds to solve the example and remember the answer.')
print("Ready?!?!")
time.sleep(2)
countdown(t)
solving()

more = input("Wanna do it one more time? y/n\n")

while more == "y":
    x1 = random.randrange(1, 100)
    x2 = random.randrange(1, 100)
    countdown(t)
    solving()
    more = input("Wanna try it one more time? y/n\n")


print('Bye!')
