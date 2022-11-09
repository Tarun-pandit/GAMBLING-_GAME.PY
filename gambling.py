print("welcome to tarun and vaibhav gambling center")
import random
computer=random.randint(1,10)
print(computer)
while True:
    a=int(input("enter your guess no:"))
    if a==computer:
                print("you win the game")
                break
    else:
     print("try again")
comp=random.randint(11,99)
print(comp)
for i in range(1,5):
    b=int(input("now gusess two digit no to win your prize money:"))
    if b==comp:
        print("you win the prize money ,congratulation")
        break

    else:
        print(f"You Have {5-i} Chances Left")
        
        
        
        
                