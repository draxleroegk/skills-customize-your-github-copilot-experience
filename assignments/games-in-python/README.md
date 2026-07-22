
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a text-based Hangman game in Python. You will practice working with strings, loops, conditionals, and user input while managing game state.

## 📝 Tasks

### 🛠️ Build the Core Game Setup

#### Description
Create the basic Hangman setup, including a predefined word list, random word selection, and variables to track guesses and remaining attempts.

#### Requirements
Completed program should:

- Define a list with at least 5 possible words.
- Randomly choose one word when the game starts.
- Create a display format for the hidden word using underscores (for example: `_ _ _ _`).
- Set a starting number of incorrect attempts (for example: 6).


### 🛠️ Implement Gameplay Loop and End Conditions

#### Description
Add the main game loop so the player can guess letters, see progress updates, and receive a clear win or lose result.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per turn.
- Reveal correctly guessed letters in all matching positions.
- Decrease remaining attempts only for incorrect guesses.
- Continue until the full word is guessed or attempts reach 0.
- Display a win message when the player guesses the word.
- Display a lose message with the correct word when attempts are exhausted.

```text
Example game output:
Word: _ _ _ _ _
Guess a letter: a
Correct! Word: _ a _ _ a
Attempts left: 6
```
