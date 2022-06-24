import random

def play():
    print("*********************************")
    print("**Welcome to the hangman game!**")
    print("*********************************")

    file = open("words.txt", "r")
    words = []
    
    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    SECRET_WORD = random.choice(words)
    alive = True
    right = False
    lives = 7
    user_word = ["_" for i in SECRET_WORD]
    wrong_letters = []

    while alive and not(right):
        print()
        print("You have {} lives".format(lives))
        print("The word so far: {}".format(" ".join(user_word)))
        print("Wrong letters: {}".format(" ".join(wrong_letters)))
        guess = input("Guess a letter: ").lower().strip()
        try:
            guess = int(guess)
            print("You can't put a number")
        except:
            if len(guess) != 1:
                print("You need to put one letter")
                continue
            for index, letter in enumerate(SECRET_WORD):
                if guess == letter:
                    user_word[index] = letter
            if "_" not in user_word:
                right = True
            if guess in wrong_letters:
                print("You have already tried the letter: {}".format(guess))
                continue
            if guess not in SECRET_WORD:
                wrong_letters.append(guess)
                lives -= 1
            if lives == 0:
                alive = False

    if right:
        print("Uhuuul! The word is {}".format(SECRET_WORD))
        print("You win")
    else:
        print()
        print("You loose!")
        print("The word was {}".format(SECRET_WORD))

    print("End of game")

if(__name__ == "__main__"):
    play()
