# Zombie Simulation - CPS310 Assignment 1

## Author
- Reese Franklin

## How to Run
1. Install Python 3 and pygame-ce: `pip install pygame-ce`
2. Run: `python main.py`
## What the Simulation Does
- 20 humans (blue) wander in random directions at random speeds.
- 3 zombies (green) chase the nearest human.
- When a zombie touches a human, they fight:
  - 40% chance the human wins and the zombie is destroyed.
  - 60% chance the human is infected and becomes a new zombie.
- The game ends when one side is wiped out, or after 45 seconds
  ("Rescue arrived!"), in which case surviving humans win.
- The counter at the top shows both populations and the timer.
- Press R to restart with a new random setup.

## Settings
All balance values are at the top of main.py:
NUM_HUMANS, NUM_ZOMBIES, FIGHT_CHANCE, TIME_LIMIT.

## Testing and Balance
- Fixed a stalemate where the last human could outrun every zombie:
  human speed was set with independent random x and y values, so
  diagonal movers were too fast. Now direction and speed are chosen
  separately, and humans are always slower than zombies.
- Added a time limit so every run ends with an outcome.
- In 5 test runs with FIGHT_CHANCE = 0.4, zombies won 3 and humans won 2.