# Rock Paper Scissors CLI Game (Python)

A simple but interactive command-line Rock Paper Scissors game built in Python with score tracking, replay system, and overall winner calculation.

## Features

- Classic Rock, Paper, Scissors gameplay
- Emoji-based visual feedback 🪨📃✂️
- Score tracking system (User vs Computer vs Tie)
- Best-of-3 match system (first to 2 wins)
- Replay option after each game session
- Final match summary with overall winner

## Tech Stack

- Python 3
- Random module (computer AI simulation)

## Project Structure

```bash
├── main.py
└── README.md
```

## How It Works

1. User selects:
   - Rock (r)
   - Paper (p)
   - Scissors (s)

2. Computer randomly selects its move

3. Game logic determines winner:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock

4. Scores are updated in real-time

5. First to reach 2 wins ends the match

6. User can choose to replay or exit

## Example Gameplay

```
Rock, Paper, or scissors? (r/p/s): r
You chose 🪨
Computer chose ✂️
You Win!

Rock, Paper, or scissors? (r/p/s): p
You chose 📃
Computer chose 🪨
You Win!

YOU WIN: 2-0
```

## Key Functions

### `get_user_choice()`
Handles and validates user input.

### `display_choices(user_choice, computer_choice)`
Displays both player and computer choices using emojis.

### `determine_winner()`
Implements game logic and updates scores.

### `play_game()`
Main game loop controlling rounds and win conditions.

### `ask_to_play_again()`
Handles replay system and final results display.

## Concepts Demonstrated

- Conditional logic
- Loops and game flow control
- Global state management
- Input validation
- Randomized decision-making
- CLI game design
- State-based scoring system

## Future Improvements

- Add GUI version (Tkinter or web-based UI)
- Add difficulty levels (smart AI instead of random)
- Add animations or delays for better UX
- Track win history across sessions
- Add multiplayer mode
- Convert into web game using Flask or React

## Learning Outcome

This project demonstrates foundational game development logic, state management, and interactive CLI design using Python.

## Author

Built by Salwa
