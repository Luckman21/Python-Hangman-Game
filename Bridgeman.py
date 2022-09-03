'''
Created on Feb 20, 2018

@author: Luqmaan, Brandon, Jason, Jazib
'''

import time, math, sys, datetime, webbrowser, os
from random import randint

print "Today is:",datetime.datetime.now()
Time1 = datetime.datetime.now()

time.sleep(2)

# loading() : Displays progress bar
def loading(load):
    Length = 50 # Length of the loading bar
    status = ""
    if load >= 1:
        load = 1
        status = "Done...\r\n" #This is the status
        return status
    bar = int(round(Length*load))
    percentage = "\rPercent  :  [{0}] {1}% {2}".format( "%" *bar+ " "*(Length-bar), load*100,status)
    
    sys.stdout.write(percentage)


# The loading bar script
for i in range(0,20):
    time.sleep(0.1)
    print "\n"*45
    loading(i*5/100.0)

print "\n"*45
print loading(100/1.0)
print "The Game is Loaded"
time.sleep(3)
print "\n"*50

#This section sets all the required variables to play the game.

#Hint is stored so it can choose a different hint depending on the value of the variable
hint = 1
#When the loop of the game breaks, this checks whether you win or lose
win = 0
#x and z are variables to position the little person on the bridge.  Depending on the value of these variables
#the position of the person will change
x = 0
z = 0

#Attempts check to see whether the number has been solved or not.  If not, then a "_" space is left in lieu
attempt_a,attempt_b,attempt_c,attempt_d = 0,0,0,0

#These are the numbers for the game.  They are randomly generated each time
num1,num2,num3,num4 = randint(0,9),randint(0,9),randint(0,9),randint(0,9)

a,b,c,d,j = "_","_","_","_",1
#print num1, num2, num3, num4

print "Bridge Man"
enter = raw_input("Press \"ENTER\" to start!")
print "\n"*50
time.sleep(2)

while j == 1:
    time.sleep(1)
    print "\nWhat do you want to do?\n\n1 - Instructions\n2 - Play"
    choose = raw_input(": ")
    
    if choose == "1":
        print "\nINSTRUCTIONS"
        print "\nWelcome to Bridge man, the ripped-off version of Hangman!  In this game, you will have to guess"
        print "the value of 4, randomly generated numbers with values from 0-9.  Each time you guess wrong, the"
        print "little person takes 1 step close off of the bridge and on to the spikes.  Your objective is to guess"
        print "all the numbers before the little person falls off of the bridge.  You are given 2 hints and if you"
        print "think your a smarty-pants, you can try to guess the whole number.  So without further adieu, its time\nto get started!\n"
    
    if choose == "2":
        j = 0
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=LYN6DRDQcjI&t=8s")
        time.sleep(5)
        
        while True:
            
            if win == True:
                break
            
            if x == 10:
                break
        
            time.sleep (1)
            win = (a == str(num1) and b == str(num2) and c == str(num3) and d == str(num4))
            print "\n" * 50
            print "", a,b,c,d,"\n"
            print (x * " ") + "\o/"
            print " =========    ="
            print "          ^^^^"
        
            if win == True:
                break
        
            print
            option = raw_input ("[1] Number\n[2] Hint %s\n[3] Entire Number\n: " % hint)
        
            if option == "1":
                l = 0
                num = raw_input ("\nEnter a number: ")
                
                if num == str(num1) and attempt_a == 0:
                    attempt_a,a,l = 1,num,1
                if num == str(num2) and attempt_b == 0:
                    attempt_b,b,l = 1,num,1
                if num == str(num3) and attempt_c == 0:
                    attempt_c,c,l = 1,num,1
                if num == str(num4) and attempt_d == 0:
                    attempt_d,d,l = 1,num,1
                if l != 1:
                    x+=1    
                
            elif option == "2":
                if hint == 1:
                    hint+=1
                    print "\nOne of the numbers has a square root of", math.sqrt(num1)
                    time.sleep (2)
                elif hint == 2:
                    hint-=1
                    print "\nOne of the numbers has a square root of", math.sqrt(num3)
                    time.sleep (2)
        
        
            elif option == "3":
                nums = raw_input("\nEnter the full number here: ")
                if nums[0] == str(num1):
                    x = 0
                else:
                    x+=1
                if nums[1] == str(num2):
                    x = 0
                else:
                    x+=1
                if nums[2] == str(num3):
                    x = 0
                else:
                    x+=1
                if nums[3] == str(num4):
                    x = 0
                else:
                    x+=1
                    
                if x > 0:
                    print "\nSorry, you guessed incorrectly."
                
                else:
                    win = True
                    a,b,c,d = str(num1),str(num2),str(num3),str(num4)
            
        browserExe = "chrome.exe"
        os.system("taskkill /f /im "+browserExe)  
        print "\n"*50
        time.sleep(2)
            
        if win == True:
            time.sleep(2)
            for y in range (0,9):
                print "\n" * 50
                print "", a,b,c,d,"\n"
                print (y * " ") + "\o/"
                print " =========    ="
                print "          ^^^^"
                time.sleep(1.5)
                z = y
            time.sleep(3)
            y = 0
            g = 0
            while True:
                y+=1
                
                if y == 1:
                    bridge = str(num1)+"   ="
                    a = "_"
                elif y == 2:
                    bridge = str(num1)+str(num2)+"  ="
                    b = "_"
                elif y == 3:
                    bridge = str(num1)+str(num2)+str(num3)+" ="
                    c = "_"
                else:
                    bridge = str(num1)+str(num2)+str(num3)+str(num4)+"="
                    d = "_"
                    g = 1
                
                print "\n" * 50
                print "", a,b,c,d,"\n"
                print (z * " ") + "\o/"
                print " ========="+bridge
                print "          ^^^^"
                time.sleep(1)
                if g == 1:
                    break
            
            time.sleep(3)
            
            for f in range (9,15):
                print "\n" * 50
                print "", a,b,c,d,"\n"
                print (f * " ") + "\o/"
                print " ========="+bridge
                print "          ^^^^"
                time.sleep(1)
                
            time.sleep(2)
            print "You Win."
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=8avMLHvLwRQ")
          
        else: 
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=8IFzTDLHuCU&t=600s")
            time.sleep (1)
            print "\n" * 50
            print "", a,b,c,d,"\n"
            print " ========= \o/="
            print "          ^^^^\nYou Lose."
            
time.sleep(10)
Time2 = datetime.datetime.now()
Total_time = str(Time2-Time1)
print "You have been playing for", Total_time, "minutes"