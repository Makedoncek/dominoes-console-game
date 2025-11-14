Here's a more natural-sounding, human-toned version of the README.

-----

# 🎲 My Python Dominoes Game

This is my take on the classic game of dominoes, built from scratch in Python. It's a full console game where you can play against a computer opponent.

I put a special focus on making the AI feel "smart." It doesn't just pick a random piece; it actually looks at the board, counts the numbers, and tries to play strategically.

##  What It Can Do

  * **A "Smart" AI Opponent:** The computer isn't just random. It scans the board and its own hand to see how "common" each number (0-6) is. It then tries to play its "highest-scoring" (most common) pieces first to keep its options open for later.
  * **Full Gameplay:** The game handles everything from shuffling and dealing the 28 dominoes to finding the first player (by looking for the highest double).
  * **Real Dominoes Rules:** You can't just play any piece you want. The game checks every move to make sure it matches the numbers on either end of the "snake." It even automatically "flips" the piece (like `[2, 5]` to `[5, 2]`) to connect properly.
  * **Handles All End-Game Scenarios:**
      * **Win/Loss:** The first player to empty their hand wins.
      * **Draw (or "Fish"):** The game correctly identifies a "locked" board—when the ends of the snake match, but all 8 pieces with that number are already on the board, so no one can play.
      * **Empty Stock:** If the "bank" (stock) runs out, players just skip their turn if they can't make a move.
  * **Clean Console UI:** The interface is simple and easy to read. If the domino snake gets too long, it automatically shortens it (e.g., `[6, 6]...[3, 4]`) so it doesn't clutter your screen.

##  How to Run It

1.  Make sure you have Python 3 installed.
2.  Clone the project:
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
    ```
3.  Go into the new folder:
    ```bash
    cd YOUR_REPOSITORY
    ```
4.  Run the game:
    ```bash
    python main.py
    ```
