import numpy as num


def welcome_message(name):
#Prints out a personalised welcome message
    return "Welcome to this Python script, " + name + "!"

#Call the welcome message function with the input "Udacity Student" 
#and print the output
#print(welcome_message("Udacity Student"))


how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Philip and Charlie
"""


#print(snake_string * how_many_snakes)

def prize(value):
    if(0<=value<=50):
        print("won rabbit")
    elif(51<=value<=100):
        print("won duck") 
    else:
        print("won nothing")
#prize(511)

list=[1,2,3,4,5,6]
#print(list[0: :2])
#print(list[1: :2])


print(num.arange(10))
