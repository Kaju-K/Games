import hangman
import guessing

def choose_game():
    print("*********************************")
    print("*******Choose your game!*******")
    print("*********************************")

    print("(1) Hangman (2) Guessing")

    game = int(input("What game do you want to play? "))

    if(game == 1):
        print("Jogando forca")
        hangman.play()
    elif(game == 2):
        print("Jogando adivinhação")
        guessing.play()

if(__name__ == "__main__"):
    choose_game()
