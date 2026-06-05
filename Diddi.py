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
        try:
        
            calc = input("Enter ur calc here -> ")
            
            ifireplacedu = the_replacer(calc)

            print(f"{ifireplacedu}")
            print(f"Before I throw an error at u sir the calc varaible is {calc}")
            print(f"Ur answer would be: {eval(ifireplacedu)}") # Eval allows code execution, will try cleanse this later

            if 'pet' in calc:
                print("We will activate cowsay nwo!11")

                
            else:
                print("Bruh what happened")
        
        except (SyntaxError, NameError , TypeError):   # Cleaner
            print(f"Pls do proper inputs")
            continue




def the_replacer(ineedtobereplaced):

    while True:
        if 'x' in ineedtobereplaced:
                print("U hit (x) if in the replacer")
                thanksforeplacingme = ineedtobereplaced.replace("x", "*")
                return(thanksforeplacingme) #Pls reutn it u literally looped it like an idiot

        elif 'X' in ineedtobereplaced:
                print("U hit (X) if in the replacer")
                thanksforeplacingme = ineedtobereplaced.replace("X", "*")
                return(thanksforeplacingme)

        elif '÷' in ineedtobereplaced:
                print("U hit (÷) if in the replacer")
                thanksforeplacingme = ineedtobereplaced.replace("÷", "/")
                return(thanksforeplacingme)
            
        else:
                print("U hit else")
                return(ineedtobereplaced)
                            
            
            

        


            

       

    

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

    
