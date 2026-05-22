import sys 
import math
import statistics
import random
import time


def theTOS():
    while True:
        print("Welcome to thy calculator, currently inputs will be from the CLI, if you want to perform certain functions eg the mean of a value you just type mean")
        time.sleep(2)
        print("Read all the instructions on the paper, do you accept the calculator TOS?  (INPUT Y OR N case sensitive)")
        TOS = str(input("- >").capitalize().strip()) # Case sensitive ppl
        if TOS == "Y":
            print("Good job")
            return TOS
        elif TOS == "N":
            print("Ok u cant use the calculator turn me on again if u feel like accepting the TOS")
            return TOS
        else:
            break # This prevents it from looping again so pls dont remove
        

def basic():
    while True:
        try:
            
            calc = input("Enter ur calc here")
            print(f"Ur answer would be {eval(calc)}")
        except SyntaxError:
            print(f"Your input of {calc} is incorrect so if u use 3x3 do 3*3")
            continue
        except NameError:
            print(f"Your input of {calc} is stupid and is probaly using non-integer numbers")
            continue
        except TypeError:
            print(f"Your input of {calc} contains brackets and sadly the integer cant handle them but soon the calculator will")
            continue
        



rootTOS = theTOS()

if rootTOS == "N":
    sys.exit()
elif rootTOS == "Y":
    print("Now I am not held accountable for silly stuff u do")

time.sleep(1)

print("We will be testing inputs with + - / and *")

time.sleep(1)

print("So a good input would be '3+3' and u get the answer below")

basic()



