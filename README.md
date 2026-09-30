# Brick Breaker Game - Pygame

A terminal-based Brick Breaker (Breakout-style) game developed using Python and Pygame.

This project was enhanced as part of the lab task by improving collision detection and adding game-end screens, replay/difficulty options, and sound feedback.

---

## Project Overview

Brick Breaker is a classic arcade-style game where the player controls a paddle to bounce a ball and destroy bricks.

The game includes:

- Player-controlled paddle
- Bouncing ball
- Destructible bricks
- Score tracking
- Lives system
- Win condition
- Game Over condition
- Replay option
- Difficulty selection
- Sound effects

---

## Technologies Used

- Python 3
- Pygame
- Object-Oriented Programming

---

## Changes Implemented

The original project was modified and enhanced through four major tasks.

### Task 1 - Improved Collision Detection

The collision detection between the ball and bricks was improved.

#### Changes Made

- Added separate handling for horizontal and vertical collisions.
- When the ball hits the **side of a brick**, the horizontal velocity (`vx`) is reversed.
- When the ball hits the **top or bottom of a brick**, the vertical velocity (`vy`) is reversed.
- This makes the ball movement more realistic and prevents incorrect bouncing.

#### Before

The ball could bounce in the wrong direction when hitting different parts of a brick.

#### After

The ball correctly determines whether the collision happened on the horizontal or vertical side and changes its direction accordingly.

---

### Task 2 - Game Over and Win Screen

A proper end-game screen was added.

#### Game Over

When the player loses all available lives:

- The game displays `GAME OVER!`
- The final score is displayed.
- The player can press `ENTER` to continue to the replay menu.
- The player can press `ESC` to exit.

#### Win

When all bricks are destroyed:

- The game displays `YOU WIN!`
- The final score is displayed.
- The player can press `ENTER` to continue.
- The player can press `ESC` to exit.

---

### Task 3 - Replay and Difficulty Selection

A replay system was added so that the player can start a new game without restarting the program.

The replay menu provides three difficulty levels:

| Option | Difficulty | Ball Speed | Paddle Width |
|--------|------------|------------|--------------|
| 1 | Easy | 3 | 120 |
| 2 | Medium | 4 | 100 |
| 3 | Hard | 6 | 80 |

There is also an exit option.

### Difficulty Behavior

#### Easy

- Slower ball
- Wider paddle
- Suitable for beginners

#### Medium

- Normal ball speed
- Normal paddle width
- Default difficulty

#### Hard

- Faster ball
- Smaller paddle
- Requires faster reactions

---

### Task 4 - Sound Feedback

Sound effects were added to improve the game experience.

The game now produces different sounds for different events:

- Wall collision
- Paddle collision
- Brick destruction
- Winning the game
- Game Over

The sounds are generated programmatically, so no external `.wav` or `.mp3` files are required.

If the system does not support audio initialization, the game continues running without sound.

---

## Project Structure

```text
brick-breaker-main/
│
├── main.py
├── requirements.txt
├── README.md
│
└── game/
    ├── game_engine.py
    ├── paddle.py
    ├── ball.py
    └── brick.py
```
## Chatgpt Chat

[View the Complete Chat](https://chatgpt.com/share/6abcee6a-ceac-83ee-9556-aa37858ba71c)

