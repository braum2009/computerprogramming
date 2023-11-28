import random
with open("sowpods.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    word = random.choice(words)
revealed_word = ""
for e in range(len(word)):
    
    revealed_word = revealed_word + "_ "


win = False
loop_word = ""
guess = ""
guess_word = "" 
attempts = 0
while attempts < 6:
    revealed_word = ""
    guess_word = ""
    
    guess = input("Guess a letter: ")
    guess = guess.upper()
    for i in range(len(word)):
        if guess == word[i] or loop_word.find(word[i]) > -1:
            revealed_word = revealed_word + word[i] + " "
            guess_word = guess_word + word[i]         
           
        else:
            revealed_word = revealed_word + "_ "
    if (guess_word == word):
        win = True
        break
    loop_word = revealed_word
    print (loop_word)
    attempts += 1
    
 
    if win == True:
        print("congradulation you won")
        again = input("Would you like to play again? y/n ")
        if again == 'y':
            attempts = 0
        else:
            print("Okay, goodbye.")
            exit()
    elif attempts == 6: 
        print("You have lost")
        again = input("Would you like to play again? y/n ")
        if again == 'y':
            attempts = 0
        else:
            print("Okay, goodbye.")
            exit()

