import random

def play_game():
  possible_outcome = ["R", "P", "S"]
  
  # validating player input using while loop
  while True:
    # getting user input
    play = input("Please pick an option between 'R', 'P' or 'S'\n")
    # converting user input to uppercase
    player = play.upper()
    if player not in possible_outcome:
      print("Invalid pick, try again.")
      continue
    else:
      print("Great move.")
      break
  # setting cpu to make a choice randomly
  computer = random.choice(possible_outcome)
  
  print(f"Player({player}) : CPU({computer})")
  for item in player:
    if player != computer:
      if player == "R":
        if computer == "S":
          print("Rock smashes scissors. Player wins!")
        else:
          print("Paper covers rock. CPU wins!")
      elif player == "P":
        if computer == "R":
          print("Paper covers rock. Player wins!")
        else:
          print("Scissors cuts paper. CPU wins!") 
      elif player == "S":
        if computer == "P":
          print("Scissors cuts paper. Player wins!")
        else:
          print("Rock smashes scissors. CPU wins!")
    elif player == computer:
      print("It's a tie.")
      play_game()
    else:
      print("Game terminated")
play_game()
     