# Battleship-Game
A command-line Battleship game developed in Python. The game generates a random battleship location on a 5×5 grid and allows players to make guesses within a limited number of attempts. The project demonstrates the use of Python lists, functions, loops, conditionals, user input handling, and random number generation.

# 🚢 Battleship Game

A command-line Battleship game developed in Python. The game generates a random battleship location on a 5×5 grid and challenges players to locate and destroy it within a limited number of attempts.

## 📖 Overview

Battleship is a classic guessing game where a hidden ship is placed on a game board. The player must guess the ship's location by entering row and column coordinates.

This project was built to practice core Python programming concepts including:

* Functions
* Lists and 2D Lists
* Loops
* Conditional Statements
* User Input Handling
* Random Number Generation
* Basic Game Logic

---

## ✨ Features

* 5×5 game board
* Random battleship placement
* Limited number of attempts
* Input validation
* Board updates after every incorrect guess
* Win and Lose conditions
* Command-line interface
* Beginner-friendly Python project

---

## 🛠 Technologies Used

* Python 3
* Python Standard Library (`random` module)

---

## 📂 Project Structure

```text
Battleship-Game/
│
├── Battleship_miniproject.py
└── README.md
```

---

## 🎮 How to Play

1. Run the Python file.
2. A hidden battleship is randomly placed on the board.
3. Enter the row number.
4. Enter the column number.
5. If your guess matches the battleship's location, you win.
6. If your guess is incorrect:

   * The guessed position is marked on the board.
   * One attempt is consumed.
7. The game ends when:

   * The battleship is destroyed, or
   * All attempts are exhausted.

---

## 🚀 Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/Kathivarshith/Battleship-Game.git
```

### Navigate to the Project Directory

```bash
cd Battleship-Game
```

### Run the Program

```bash
python Battleship_miniproject.py
```

---

## 🖥 Sample Output

```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

Guess the Row Position of the battleship: 2
Guess the Column Position of the battleship: 3

That was a close shot but not good enough...

0 0 0 0 0
0 0 X 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

---

## 🧠 Concepts Demonstrated

### Functions

The project uses functions to organize the game logic:

* Board initialization
* Board display
* Guess tracking
* Pattern updates

### 2D Lists

The game board is implemented using a two-dimensional list:

```python
PATTERN = [
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
```

### Random Number Generation

The battleship location is generated randomly:

```python
X = random.randint(1, Rows)
Y = random.randint(1, Rows)
```

### Input Validation

The program checks whether user-entered coordinates fall within the valid game board range.

---

## 🔮 Future Improvements

Potential enhancements for future versions:

* Prevent duplicate guesses
* Add multiple battleships
* Difficulty levels
* Scoring system
* Turn counter
* Colored terminal output
* Graphical User Interface (GUI)
* Multiplayer mode
* Save and load game progress

---

## 📈 Learning Outcomes

This project helped develop skills in:

* Problem-solving
* Algorithmic thinking
* Python fundamentals
* Data structures
* Game development basics
* Code organization using functions

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 👨‍💻 Author

**Kathivarshith

GitHub Repository:

https://github.com/Kathivarshith/Battleship-Game

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

---

## 📄 License

This project is open-source and available under the MIT License.
