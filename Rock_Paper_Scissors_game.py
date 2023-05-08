#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

Game = ['r', 'p', 's']
player_points = 0
computer_points = 0
chances = 1
print("Hi! Welcome to my Rock Paper Scissors Game")
print("Choose\nr for Rock\np for Paper\ns Scissors\n")

while (chances <= 5) :
    a = input("Your turn\n")
    choice = random.choice(Game)
    print(choice)
    if a == choice:
        print("Opps its a tie")
        print("Both got 0 points")

    elif a == "r" and choice == "s":
        player_points = player_points + 1
        print("YOU WON")
        print("you got 1 point")

    elif a == "p" and choice == "r":
        player_points = player_points + 1
        print("YOU WON")
        print("you got 1 point")

    elif a == "s" and choice == "p":
        player_points = player_points + 1
        print("YOU WON")
        print("you got 1 point")

    elif a == "r" and choice == "p":
        computer_points = computer_points + 1
        print("TRY AGAIN")
        print("computer got 1 points")

    elif a == "p" and choice == "s":
        computer_points = computer_points + 1
        print("TRY AGAIN")
        print("computer got 1 points")

    elif a == "s" and choice == "r":
        computer_points = computer_points + 1
        print("TRY AGAIN")
        print("computer got 1 points")

    else:
        print("You Enter wrong input")

    print(5 - chances, "chances left")
    chances = chances + 1

if chances > 5:
    print("GAME OVER")

if computer_points > player_points :
    print("computer wins")
elif computer_points < player_points:
    print("You won this game")
else:
    print("its a tie")

print(f"your points is {player_points} and computer points is {computer_points}")

