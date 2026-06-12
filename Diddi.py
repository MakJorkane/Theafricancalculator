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
        
def basic(asumoo):
    while True:
        try:
        
            calc = input("Enter ur calc here -> ")
            formoocombination = "null"



            if 'pet' in calc:
                print("We will activate cowsay nwo!11")
                moowoo = the_cowsay(calc)
                print(f"Ur new pet is now {moowoo}")
                basic(moowoo) # Or else it tries to execute the calculation when the user has not had an input


            elif 'x' or 'X' or '÷':
                calc = the_replacer(calc)

            elif moowoo is not None:
                print(f"Ur answer would be according to the {moowoo}:")
                formoocombination = (f"{eval(calc)}") 
                print(f"{cowsay(moowoo)(formoocombination)}")
                
                # {cowsay(moowoo)}{eval(calc)}")
                


                
            else:
                print("Bruh what happened")

            

            # print(f"{moowoo}")
            print(f"Before I throw an error at u sir the calc varaible is {calc}")
            print(f"Ur answer would be: {eval(calc)}") # Eval allows code execution, will try cleanse this later
            time.sleep(2)
            # Split up u can delete this depending on what the result is
            print("Now I will force print the moowoo because its lowkey forced")
            print(f"Does it print at the root function?!?!?!?!?!?!??! {asumoo}")
            
            
            if asumoo in cowsay.char_names: # Holy this is peak level intellgence
                formoocombination = (f"{eval(calc)}")   # Calculates inout and assigns it to foomoocombination

                getattr(cowsay, asumoo)(formoocombination)
        
        except ():   # Cleaner
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
        
def the_cowsay(iwanttomoo):
     print("Ok so basically u can pick a pet so which one do u want")
     time.sleep(1)
     print(f"U can pick from {cowsay.char_names}")
     print(f"{iwanttomoo}")
     time.sleep(5)
     

     while True:

        pickthypet = input("What pet u lowkey what??? -> ")
        

        if 'beavis' in pickthypet:
            print("U picked beavis")
            return pickthypet
            

        elif 'cheese' in pickthypet:
            print("U picked cheese")
            return pickthypet
            break
        
        elif 'cow' in pickthypet:
            print("U picked cow")
            return pickthypet
            break
        
        elif 'daemon' in pickthypet:
            print("You picked daemon")
            return pickthypet
            break
        
        elif 'dragon' in pickthypet:
            print("You picked the dragon")
            return pickthypet
            break
        
        elif 'fox' in pickthypet:
            print("You picked the fox")
            return pickthypet
            break
        
        elif 'ghostbusters' in pickthypet:
            print("You pick ghostbusters scary!11")
            return pickthypet
            break

        elif 'kitty' in pickthypet:
            print("You picked the kitty")
            return pickthypet
            break

        elif 'meow' in pickthypet:
            print("You picked the meow")
            return pickthypet
            break

        elif 'miki' in pickthypet:
            print("You picked miki")
            return pickthypet
            break
        
        elif 'octopus' in pickthypet:
            print("You picked the ocotpus")
            return pickthypet
            break

        elif 'pig' in pickthypet:
            print("You picked the pig")
            return pickthypet
            break
        
        elif 'stegosaurus' in pickthypet:
            print("You picked the stegosaurus")
            return pickthypet
            break

        elif 'stimpy' in pickthypet:
            print("You picked the stimpy")
            return pickthypet
            break

        elif 'trex' in pickthypet:
            print("You picked the trex")
            return pickthypet
            break

        elif 'turkey' in pickthypet:
            print("You picked the turkey")
            return pickthypet
            break

        elif 'turtle' in pickthypet:
            print("You picked the turtle")
            return pickthypet
            break

        elif 'tux' in pickthypet:
            print("You picked tux which is like linux")
            return pickthypet
            break
        
        else:
            print("Pick a valid pet pls")
    
print("We have broken out!!!!!")
    
            
         

         

        


    
     
                        
rootTOS = theTOS()

if rootTOS == "N":
    sys.exit()
elif rootTOS == "Y":
    print("Now I am not held accountable for silly stuff u do")

time.sleep(1)

print("We will be testing inputs with + - / and *")

time.sleep(1)

print("So a good input would be '3+3' and u get the answer below")

basic(asumoo="I DONT NEED IT")

ilookfor = set("X x ÷" .split())

    
