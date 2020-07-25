from gameCodes import GuessingGame as gg
from gameCodes import ChoosingGame as cg

class StartApp:
  input("Please click enter to Proceed: \n")
  inp=0
  while True:
    if inp==1:
      gg.GuessingGame.startGame()
    elif inp==2:
      cg.ChoosingGame.startGame()
    elif inp==99:
      break
    print("Please select a game... You can choose one by entering the number corresponding to the game\n1...\tThe Guessing Game\n2...\tThe Choosing Game\n99... To Exit THe Game.")
    inp = int(input("Please Enter the Game number: ")) 
