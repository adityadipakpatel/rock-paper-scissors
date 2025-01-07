# Rock-Paper-Scissors 🎮

A Python implementation of the classic Rock-Paper-Scissors game with a twist! This version incorporates a scientifically-backed strategy to increase the computer's odds of winning to over **75%** against human players.

## How It Works
This game leverages two key strategies:
1. **Psychological Manipulation**:  
   Before each game, a random distracting question is asked to subtly influence the player's choice. Studies suggest people are more likely to choose "Scissors" when distracted, so the computer opens with "Rock" for the first move.
   
2. **Pattern-Based Response**:  
   Based on research analyzing 54,000 games, human players exhibit predictable behavior:
   - If they **win**, they're more likely to repeat the same choice.
   - If they **lose**, they tend to shift to the next option in the sequence of **Rock -> Paper -> Scissors**.
   - Using this insight:
     - The computer moves **forward in the sequence** if it wins.
     - The computer moves **backward in the sequence** if it loses.
     - The computer repeats its choice if it's a tie.

These combined strategies give the computer a **significant edge**, making it a formidable opponent!

## How to Play
1. Run the game.
2. Answer a random question (just for fun!) and then choose **Rock**, **Paper**, or **Scissors**.
3. See if you can outsmart the computer's strategy!

## Features
- **Interactive Gameplay**: A fun mix of gameplay and psychology.
- **Dynamic Strategy**: The computer adapts to your choices in real time.
- **Challenging Opponent**: With a winning probability of over 75%, the computer is hard to beat!

## Prerequisites
- Python 3.x installed on your machine.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/adityadipakpatel/rock-paper-scissors.git
   ```
2. Navigate to the folder:
   ```bash
   cd rock-paper-scissors
   ```
3. Run the game:
   ```bash
   python3 rock-paper-scissors.py
   ```

## Example Gameplay
```plaintext
Welcome to Rock-Paper-Scissors!
Let's play! I have a strategy, but can you beat me?

What's your favorite color?

Now, choose Rock, Paper, or Scissors (or type 'exit' to quit): Scissors

You chose: Scissors
Computer chose: Rock
I win this round!

---
```

## Winning Strategy Breakdown
The computer's logic is simple but effective:
1. **First Move**: Always "Rock" to capitalize on the user's likely choice of "Scissors."
2. **Subsequent Moves**:
   - **Win**: Move forward in the sequence (e.g., Rock -> Paper -> Scissors).
   - **Lose**: Move backward in the sequence (e.g., Scissors -> Paper -> Rock).
   - **Tie**: Repeat the same choice.

By exploiting human tendencies, this strategy increases the computer's chances of winning significantly(~75%)!

## License
This project is licensed under the MIT License.

## Reference
The winning strategy and psychology behind it were inspired by a study discussed in this [YouTube video](https://youtu.be/Twn_4AW0M6U) from **13:00 min to 15:00 min**.

---

Will you be able to outsmart the machine? Play now and find out! 🎮

