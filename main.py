import random
import hangman_words
import hangman_art

print(hangman_art.logo)

total_lives=6
lives=6
chosen_word=random.choice(hangman_words.word_list)
placeholder=""
for letter in chosen_word:
    placeholder+="_"


game_not_over=True


guessed = ""
display = ["_"]*len(chosen_word)
while game_not_over:
    print("Word to guess: " + placeholder)
    guess=input("Guess a letter: ")
    if guess in guessed:
        print("You've already guessed " + guess)
        continue
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                display[i]=guess
                guessed+=guess
        print("Nice guess!")
    else:
            lives-=1
            print("You guessed " +guess+",that's not in the word. You lose a life.")



    print(hangman_art.stages[lives])
    if lives <= 0:
        game_not_over = False
        break
    print("******************** "+str(lives)+"/"+str(total_lives)+" left *************************")

    placeholder="".join(display)


if not game_not_over:
    print("******************** IT WAS "+chosen_word+ " ! YOU LOSE *************************")

