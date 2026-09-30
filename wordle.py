"""
******************************
CS 1026A Fall 2025
Assignment 2: Wordle
Created by: Mariya Maksymenko
Student ID: mmaksym
Student Number: 251521248
File created: October 20, 2025
******************************
This file is going to make a word guessing game similar to Wordle.
"""
from randwords import get_rand_word

def guess_word(length):
    #checks if the guess is the same length as the actual word
    #if not it returns an empty string
    guess = input(f"Enter your guess: ")
    if len(guess) != length:
        print("Incorrect length.")
        return ""
    else:
        return guess.upper()

def check_guess(guess, actual):
    #shows which letters are correct or in the wrong position
    #creates a list for clue with "^"
    clue = ["^"]*len(actual)
    #creates a list with the actual word
    actual_list = list(actual)
    length = int(len(guess))
    #first pass - check for exact matches
    for i in range(length):
        if actual[i] == guess[i]:
            #if there is a match, replaces the "^" in clue with a "!" at index i to show the exact letter has been found
            clue[i] = "!"
            #removes the letter from the actual list so it doesn't get marked again
            actual_list[i] = None

    #second pass - check for partial matches
    for i in range(length):
        #if the letters been found, just moves on
        if clue[i] == "!":
            continue

        if guess[i] in actual_list:
            #if the letter is in the word, replaces the "^" with "*"
            clue[i] = "*"
            #finds the index where the letter guess[i] appears in the actual word
            position = actual_list.index(guess[i])
            #cross it off in the actual word so it's not flagged again
            actual_list[position] = None
    return "".join(clue)

def play_game(actual=""):
    LENGTH = len(actual)
    print("Welcome to Wordle!")
    print(f"The word length is {LENGTH}.")
    i = 0
    while i<6:
        guess1 = guess_word(LENGTH)
        #checks if the guess is the correct length
        #if not, it skips the rest of the loop and doesn't count it toward the 6 guesses
        if guess1 == "":
            continue
        #adds one to the total number of guesses after a valid guess has been made
        i += 1
        check1 = check_guess(guess1, actual)
        print(f"Guess #{i}: {guess1}")
        print(check1)
        #checks if the user has guessed the word correctly
        #if so, ends the program
        if check1 == "!" * LENGTH:
            print(f"You won!\nYou guessed it in {i} guesses!")
            return
    #prints if user doesn't guess the word in 6 guesses
    print("You lost :(")
    print(f"The word was {actual}.")
