import random

name=input("What is your name?")
print("Welcome", name)
print("!!! Hangman Game !!!")

print("We ask you a movie")
print("You can make 7 mistakes")

movies = ["FIGHTCLUB", "MATRIX", "ANABEL"]
question = random.choice(movies)

print(question)
questionsletter=set(question)
guessed_letters = []
correctguesses=set()

counter = 0
win=0
while counter < 7 and win==0:

    if correctguesses.union(questionsletter)!=correctguesses:
        letter = input("Please enter a letter:")
        letter = letter.upper()
        if letter not in guessed_letters:
            guessed_letters.append(letter)
            if letter in question:
                print("Congratualations, ", letter, "is in the name of the movie")
                correctguesses.add(letter)
            else:
                print(("Wrong answer!"))
                counter+=1
    else:
        print("You won !!!")
        win+=1
        exit()
    print(correctguesses)
    print(questionsletter)
if counter == 7:
    print("You lost :(")
    exit()







