# Treasure Island Game 

A **text-based adventure game** built using Python where the player makes choices to navigate through a mysterious island in search of hidden treasure.  
Each decision affects the outcome, making the game interactive and replayable.

---

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Game Flow](#game-flow)
- [How It Works](#how-it-works)
- [Concepts Covered](#concepts-covered)

---

## Features

- Interactive **choice-based gameplay**
- Multiple decision paths leading to:
  - Victory 
  - Game Over 
- Input validation with clear feedback
- Replay option after each game session
- Beginner-friendly Python logic
- Clean and readable console output

---

## Usage

1. Run the program:
```bash
python treasure_island.py
```
2. Follow the instructions shown in the console.
3. Make choices carefully — your decisions decide your fate!
4. Replay the game as many times as you like.

---

## How to Play
1. Start at a crossroads:
* Choose left or right
2. If you go left:
* Decide whether to wait or swim
3. If you wait:
* Choose one of three doors:
    * Red
    * Blue
    * Yellow
4. One door leads to treasure, others lead to danger.
5. Any wrong decision results in Game Over.
6. After the game ends, choose whether to play again.

---

## Game Flow
```
Start
 └── Crossroad
     ├── Right → Fall into hole → GAME OVER
     └── Left
         ├── Swim → Attacked → GAME OVER
         └── Wait
             ├── Red Door → Fire → GAME OVER
             ├── Blue Door → Beasts → GAME OVER
             └── Yellow Door → Treasure → YOU WIN
```

---

## How It Works
1. The game logic is encapsulated inside a function (treasure_island)
2. Uses:
* input() for player choices
* if-elif-else for decision branching
3. .strip().lower() ensures input consistency
4. A while True loop allows replaying the game
5. Clear messages guide the user at every step

---

## Concepts Covered
* Functions
* Conditional statements (if, elif, else)
* User input handling
* String methods (strip, lower)
* Loops (while)
* Control flow logic
* Text-based game design

---
