import random
'''
1 = snake 
-1 = water
0 = gun
'''

computer = random.choice([-1, 0, 1])
youatr = input("Enter your choice : ")
youDict = {"s" : 1 ,"w" : -1 , "g" : 0}
reverseDict = {1: "snake" , -1 : "water", 0 : "gun"}

you = youDict[youatr]
print(f"you choice {reverseDict[you]}\ncomputer chocie {reverseDict[computer]} ")

if (computer == you):
    print("Draw")
else:    
    if(computer == -1 and you == 1):
        print("You win !" ) 
    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == -1):
     print("You lose!")
    elif(computer == 1 and you ==0):
     print("You win !")

    elif(computer == 0 and you == 1):
        print("You lose")
    elif(computer == 0 and you == -1):
        print("You win!")            

    else:
        print("Somthing Went Wrong")