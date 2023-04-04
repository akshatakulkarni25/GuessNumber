
from art import logo
import random
import os

def play_game(chance):
  game_over=False
  while(chance and not game_over):
    print(f"You have {chance} attempts remaining to guess the number")
    user_guess = int(input("Make a guess: "))
    chance -=1
    if (user_guess == chosen_number):
      print(f"YAY!! You got it! The answer was {user_guess}.")
      game_over=True
    elif (chance==0):
      print(f"You lose. The number was {chosen_number}")
    elif(user_guess<chosen_number):
      print("Too low.Go higher.\nGuess Again")
    elif(user_guess>chosen_number):
      print("Too high.Go lower.\nGuess Again")



play = True
while play:
  print(logo)
  print("Welcome to the Number Guessing Game")
  print("I'm thinking of a number between 1 and 100. Can you guess the number??")
  chosen_number=random.randint(1,100)
  level = input("Choose difficulty level. Type 'easy' 'medium' or 'hard':\n")
  if(level == 'easy'):
    chances = 10
  elif (level == 'medium'):
    chances = 7
  elif(level == 'hard'):
    chances = 5
  
  play_game(chance=chances)
  if input("Do you want to play again. Type 'yes' or 'no'.") == 'yes':
    os.system('clear')
    play=True
  else:
    play=False