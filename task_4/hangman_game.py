# HANGMAN GAME

import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'pineapple']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def hangman():
    word_to_guess = choose_word()
    guessed = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1
            print(f"Attempts left: {attempts}")

        display = display_word(word_to_guess, guessed)
        print(display)

        if '_' not in display:
            print("Congratulations! You've guessed the word!")
            break

    if '_' in display:
        print(f"Sorry, the word was: {word_to_guess}")

hangman()
