# cows-and-bulls-game
A classic number-guessing logic game built in Python. The program generates a random 3-digit number with no repeating digits, and the player has 8 attempts to guess it correctly.

## How It Works

- The computer picks a random 3-digit number (digits 1-9 for the first digit, 0-9 for the rest, no repeats).
- The player enters guesses, and after each guess, the game gives feedback:
  - *KACCHAN* = number of digits that are correct and in the correct position (i.e. "bulls")
  - *DEKU* = number of digits that are correct but in the wrong position (i.e. "cows")
- The player has 8 tries to guess the exact number and win.

> Fun detail: digit counts are named "Kacchan" and "Deku" as a nod to My Hero Academia — Kacchan (exact matches) and Deku (partial matches).

## Skills Demonstrated

- Random number generation without repetition (random.sample, random.choice)
- Input validation using recursion (rejects invalid/repeated-digit input and re-prompts)
- List indexing and comparison logic
- String/int type handling and conversion
- Loop control with early exit conditions (break)

Play instantly in your browser - https://trinket.io/python/cb6ca96e82eb?outputOnly=true&runOption=run&showInstructions=true
