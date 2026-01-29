# Hangman Game (Multi-Level Console Version)

A **Python console-based Hangman game** featuring **multiple difficulty levels**, **lives management**, **time-based scoring**, and **progressive difficulty**. The game becomes more challenging as the player wins and allows replay without restarting the program.

---

## Table of Contents

* [Features](#features)
* [Game Rules](#game-rules)
* [Usage](#usage)
* [How It Works](#how-it-works)
* [Difficulty Levels](#difficulty-levels)
* [Concepts Covered](#concepts-covered)
---

## Features

* Classic Hangman gameplay
* Three difficulty levels with increasing complexity
* Dynamic word selection based on level
* Limited lives per level
* Time-based scoring system
* Replay option without restarting the program
* Input validation for better user experience
* Clear win/lose feedback

---

## Game Rules

* Guess **one letter at a time**
* Each incorrect guess reduces **one life**
* Words become **longer and harder** as levels increase
* Faster completion results in a **higher score**
* Game resets to Level 1 after a loss
* You can replay the game anytime

---

## Usage

1. Run the program:

```bash
python hangman.py
```

2. Read the rules and press **Enter** to start.

3. Guess letters until you:

* Complete the word (win), or
* Run out of lives (lose)

4. Choose whether to replay after each round.

---

## How It Works

* Words are stored in a dictionary mapped to difficulty levels.
* Each level has a predefined number of lives.
* The game tracks:

  * Guessed letters
  * Remaining lives
  * Time taken to complete the word
* Score is calculated using:

```
Score = (Remaining Lives × 100) − Time Taken
```

* Winning increases difficulty; losing resets progress.

---

## Difficulty Levels

| Level | Word Type             | Lives |
| ----- | --------------------- | ----- |
| 1     | Short & simple words  | 6     |
| 2     | Medium-length words   | 5     |
| 3     | Long & advanced words | 4     |

---

## Concepts Covered

* Python functions and modular design
* Dictionaries and lists
* Loops and conditional logic
* Random selection
* Time tracking and scoring
* Input validation
* Game state management

---
