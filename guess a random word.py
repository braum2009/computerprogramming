word = 'happy'
loop_word = "_ _ _ _ _  "
guess = ""
guess_word = "" 
while True:
    revealed_word = ""
    guess_word = ""
    
    guess = input("Guess a letter: ")
    for i in range(len(word)):
        if guess == word[i] or loop_word.find(word[i]) > -1:
            revealed_word = revealed_word + word[i] + " "
            guess_word = guess_word + word[i]         
           
        else:
            revealed_word = revealed_word + "_ "
    if (guess_word == word):
        break
    loop_word = revealed_word
    print (loop_word)
    
print("congradulation you won") 