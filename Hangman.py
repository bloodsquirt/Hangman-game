import random
def hangman():
    wordlist = ["panda", "elephant", "gorilla", "doge", "tiger", "platypus", "raindeer", "mammoth", "cheetah", "giraffe", "leapord","unicorn", "duck", "sloth", "babbon"]
    word = random.choice(wordlist)
    validletter='abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("Congratulations,You won!")
            break

        print("Guess the word: ",main)
        guess = input()

        if guess in validletter:
            guessmade = guessmade + guess
        else:
            print("Please enter a valid letter")
            guess = input()

        if guess not in word:
            turns= turns - 1
            if turns == 9:
                print("9 turns left!")
                print("  ------  ")
            if turns == 8:
                print("8 turns left!")
                print("  ------  ")
                print("     |    ")
            if turns == 7:
                print("7 turns left!")
                print("  ------  ")
                print("     |    ")
                print("     O    ")
            if turns == 6:
                print("6 turns left!")
                print("  ------  ")
                print("     |    ")
                print("     O    ")
                print("     |    ")
            if turns == 5:
                print("5 turns left!")
                print("  ------  ")
                print("     |    ")
                print("     O    ")
                print("     | \  ")
            if turns == 4:
                print("4 turns left!")
                print("  ------  ")
                print("     |    ")
                print("     O    ")
                print("   / | \  ")
            if turns == 3:
                print("3 turns left!")
                print("  ------  ")
                print("     |    ")
                print("     O    ")
                print("   / | \  ")
                print("      \   ")
            if turns == 2:
                print("2 turns left!")
                print("  ------  ")
                print("     |    ")
                print("     O    ")
                print("   / | \  ")
                print("    / \   ")
            if turns == 1 :
                print("1 turns left!")
                print("  ------  ")
                print("    _|_   ")
                print("   |_O_|  ")
                print("   / | \  ")
                print("    / \   ")
            if turns == 0 :
                print("Sorry, You lost the game!")
                print("  ------  ")
                print("    _|_   ")
                print("   |_O_|  ")
                print("   | | |  ")
                print("    | |   ")
                break

name = input("Enter your name: ")
print("Welcome % s"%name)
print("----------------------------------------------------------------")
print("Try to guess the word in 10 attempts")
hangman()


