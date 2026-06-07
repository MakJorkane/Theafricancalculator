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
                moowoo = the_cowsay(calc)

                
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
        
        elif 'pet' in ineedtobereplaced:
             print("Wow time 2 go to cowsay")
             the_cowsay(ineedtobereplaced)


            
        else:
                print("U hit else")
                return(ineedtobereplaced)
        
def the_cowsay(iwanttomoo):
     print("Ok so basically u can pick a pet so which one do u want")
     time.sleep(1)
     print(f"U can pick from {cowsay.char_names}")
     print(f"{iwanttomoo}")
     time.sleep(5)
     pickthypet = input("What pet u lowkey what???")

     if 'beavis' in pickthypet:
        print("U picked beavis")
    
     elif 'cheese' in pickthypet:
        print("U picked cheese")
    
     elif 'cow' in pickthypet:
        print("U picked cow")
     
     elif 'daemon' in pickthypet:
        print("You picked daemon")
     
     elif 'dragon' in pickthypet:
        print("You picked the dragon")
     
     elif 'fox' in pickthypet:
        print("You picked the fox")
     
     elif 'ghostbusters' in pickthypet:
        print("You pick ghostbusters scary!11")

     elif 'kitty' in pickthypet:
        print("You picked the kitty")

     elif 'meow' in pickthypet:
        print("You picked the meow")

     elif 'miki' in pickthypet:
        print("You picked miki")
    
     elif 'octopus' in pickthypet:
        print("You picked the ocotpus")

     elif 'pig' in pickthypet:
        print("You picked the pig")
     
     elif 'stegosaurus' in pickthypet:
         print("You picked the stegosaurus")

     elif 'stimpy' in pickthypet:
         print("You picked the stimpy")

     elif 'trex' in pickthypet:
         print("You picked the trex")

     elif 'turkey' in pickthypet:
         print("You picked the turkey")

     elif 'turtle' in pickthypet:
         print("You picked the turtle")

     elif 'tux' in pickthypet:
          print("You picked tux which is like linux")
         

         

        


    
     
                        
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

    
