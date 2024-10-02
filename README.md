This repository contains a Python implementation of a simple slot machine game. The player can place bets, spin the slot machine, and win or lose money based on the outcomes.

Features

  Slot Machine Spin: The game simulates a 3x3 slot machine grid with different symbols.
  Betting: The player can place bets within a specified range.
  Winning Lines: The player wins if symbols match on any line. The game checks for matches across the rows.
  Payout System: Each symbol has a value, and the payout is determined based on the value of the matching symbol and the player's bet.

Game Rules
  There are 3 rows and 3 columns in the slot machine grid.
  The player can place a bet between 1 and 100 units.
  Symbols have varying frequencies and values:
  Symbol A: Appears 2 times, value is 5.
  Symbol B: Appears 4 times, value is 4.
  Symbol C: Appears 6 times, value is 3.
  Symbol D: Appears 8 times, value is 2.
  If all symbols in a row match, the player wins. The payout is calculated as symbol value * bet.
