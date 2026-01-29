# Heads or Tails Game (Python Console Game)

A **Python-based console game** that simulates a **Heads or Tails coin toss** with support for **multiple tosses, user predictions, and detailed game statistics**.  
The project demonstrates randomness, user interaction, loops, and basic statistical calculations.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Game Statistics](#game-statistics)
- [How It Works](#how-it-works)
- [Concepts Covered](#concepts-covered)

---

## Features

- User can choose **Heads or Tails**
- Supports **multiple coin tosses** in one round
- Displays result of each toss
- Tracks:
  - Total tosses
  - Wins
  - Losses
  - Win rate percentage
- Input validation for:
  - Choice (Heads/Tails)
  - Number of tosses
- Option to play multiple rounds
- Simple and interactive console interface

---

## Usage

1. Run the program:
```bash
python heads_or_tails.py
```
2. Choose:
* h for Heads
* t for Tails
3. Enter how many times you want to toss the coin.
4. View results and statistics.
5. Decide whether to play again.

---

## How to Play
1. Select your prediction (Heads or Tails).
2. Enter the number of coin tosses.
3. The program randomly tosses the coin multiple times.
4. Each toss result is displayed.
5. Wins and losses are calculated based on your prediction.
6. Overall statistics are shown after each round.

---

## Game Statistics
After each round, the following statistics are displayed:
* Total Tosses – Total number of coin tosses across all rounds
* Wins – Number of times the user's prediction was correct
* Losses – Number of times the prediction was incorrect
* Win Rate – Percentage of correct predictions

---

## How It Works
1. Uses Python’s random module to simulate coin tosses
2. The game runs inside a while loop for continuous play
3. User inputs are validated to prevent invalid choices
4.Statistics are stored and updated across multiple rounds
5. Win rate is calculated using basic percentage formula

---

## Concepts Covered
* Random number generation (random.choice)
* Loops (while, for)
* Conditional statements
* User input handling and validation
* Basic statistics calculation
* String formatting
* Console-based game logic

---
