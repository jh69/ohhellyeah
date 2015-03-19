#!/usr/bin/python
import random, time
timestorun = 100
string = ""
capson = 0
       
def makemore(letter, freq):
        global string
        if random.random() < freq:
                string = string + letter
                makemore(letter, freq)
 
def makephrase():
        global string
#90% chance of oh
        if random.random() < 0.9:                      
                string = string + " o"
                makemore("o", 0.6)
                string = string + "h"
                makemore("h", 0.6)
 
#90% chance of hell yeah
        if random.random() < 0.9:
                string = string + " hell y"
                makemore("y", 0.3)
                makemore("e", 0.8)
                makemore("a", 0.8)
                makemore("h", 0.7)
 
#60% chance of baby
        if random.random() < 0.6:      
                string = string + " baby"
                makemore("y", 0.3)
       
#60/40 !/.
        if random.random() < 0.6:
                string = string + "!"
                makemore("!", 0.925)
        else:
                string = string + "."
                makemore(".", 0.8)
        string = string + " "
 
#50/50 chance of caps  
        capson = random.random()
        if capson > 0.5:
                string = string.upper()
        time.sleep(0.1)
        print string
        string = ""
       
       
i = 0
while i < timestorun:
        makephrase()
        i += 1
