from helpers import draw_board, check_turn, check_for_win
import os
# importing the os will prevent from the board being printed on the console everytime the player makes a move

# using a dictionary to create keys for the different spots a player can take so that it can be updated with an X or O

spots = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

playing = True
complete = False
turn = 0
prev_turn =-1

while playing:
  os.system('cls' if os.name == 'nt' else 'clear')
  draw_board(spots)
  if prev_turn == turn:
    print("Invalid spot selected! Please pick another spot.")
    prev_turn = turn
  print("Player " + str(turn % 2 + 1) + "'s turn: Pick your spot or press E to exit/quit the game")
  # get input from player
  choice = input()
  if choice == 'E':
    playing = False
    # check if the player gave a valid input from 1-9
  elif str.isdigit(choice) and int(choice) in spots:
    # check if the spot that the playere chose was already taken by the other player
    if not spots[int(choice)] in {"X", "O"}:
      turn += 1
      spots[int(choice)] = check_turn(turn)
  # check if game is finished
  if check_for_win(spots): playing, complete = False, True
  if turn > 8: playing = False


os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if complete:
  if check_turn(turn) == 'X': print("Player 1 Wins!")
  else: print("Player 2 Wins!")
else:
  #tied game
  print("No winners! It's a tie!")

print("Thanks for playing!")
