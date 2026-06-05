import sys 
import math
import statistics
import random
import time
import cowsay
import re #should help with cleaner user inputs

def theTOS():
    print("Welcome to thy calculator, currently inputs will be from the CLI, if you want to perform certain functions eg the mean of a value you just type mean")
    while True:
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
            pass # This prevents it from looping again so pls dont remove
        

def basic():
    while True:
        try:  # Keep this in the try statement to handle errors
        
            calc = input("Enter ur calc here -> ")
            
            the_replacer() == calc

            if 'pet' in calc:
                print("We will activate cowsay nwo!11")

                
            else:
                tempcorrection = re.search("^÷.*X$", calc)
                print(f"Ur answer would be: {exec(calc)}") # Eval allows code execution, will try cleanse this later
                    
    

        except (SyntaxError, NameError , TypeError):   # Cleaner
            print(f"Pls do proper inputs")
            continue


def the_replacer(e):

    while True:
        if 'x' in e:
                re.sub('x', '*', e)

        elif 'X' in e:
                re.sub('X', '*', e)

        elif '÷' in e:
                re.sub('÷', '*', e)
            
        else:
                return            
            
            

        


            

       

    

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

ilookfor = set("X x ÷" .split())

    
