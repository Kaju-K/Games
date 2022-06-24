import random

def play():

    print("*********************************")
    print("Welcome to the game of guessing!")
    print("*********************************")

    secret_number = random.randrange(1,101)
    number_of_guesses = 0
    score = 1000

    print("Dificulties")
    print("(1) Easy (2) Normal (3) Hard")

    level = 0
    while level == 0:
        level_str = input("Define the dificulty: ")
        try:
            level = int(level_str)
        except:
            print("You should put a number")
        else:
            if level < 1 or level > 3:
                print("The number should be between 1 and 3. Try it again.")
                level = 0


    if level == 1:
        number_of_guesses = 20
    elif level == 2:
        number_of_guesses = 10
    else:
        number_of_guesses = 5

    for round in range(1, number_of_guesses + 1):
        print("Guess {} out of {}".format(round, number_of_guesses))

        guess_str = input("Type a number between 1 and 100: ")
        print("Você digitou " , guess_str)
        guess = int(guess_str)

        if (guess < 1) or (guess > 100):
            print("You must type a number between 1 and 100!")
            continue

        right = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if right:
            print("You are right and scored {}!".format(score))
            break
        else:
            if bigger:
                print("You are wrong! Your guess was bigger than the secret number.")
            elif smaller:
                print("You are wrong! Your guess was smaller than the secret number.")
            lost_points = abs(secret_number - guess)
            score = score - lost_points
            if round == 5:
                print("The secret number was {}".format(secret_number))
    
    print("End of game")

if(__name__ == "__main__"):
    play()
