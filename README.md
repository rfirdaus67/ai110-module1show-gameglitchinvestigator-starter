# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Game's purpose: A number guessing game where the user inputs a number and the game will give hints (if the user chooses) depending on how close the guess is to the secret number

- Bugs: Found multiple bugs, including the "New Game" button not starting a new game, the attempts not initially starting at 0, the hints being backwards, the score not being calculated properly, and more

- Fixes applied: I fixed the hints being backwards simply by switching their output messages. So when the guess was too high, the hint told the user to "go lower" and vice versa. I fixed the attempts not starting at 0 by making st.session_state.attempts = 0 instead of 1. I fixed the new game starting by clearing the history and setting the status back to "playing" so the program knew a new game was starting. Also fixed the issue of the hints not showing properly when st.rerun was added to decrement the "Attempts Left" after the first guess, still giving the user the number of attempts needed. I did this by storing the message to be displayed and moving it out of the "if submit..." block so they would not interfere with each other.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. On Normal mode, user starts with 8 guesses
2. User enters a guess of 50
3. Game returns "Go LOWER!"
4. User enters a guess of 15
5. Game returns "Go HIGHER!"
6. After each guess, the attempts left decrements
7. Game ends after attempts left = 0 or user guesses correctly
8. User gets a score that updates based on whether they lost or guessed correctly

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
========================== test session starts ==========================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/rehanafirdaus/Desktop/CodePath/ai110-module2/project1
collected 6 items                                                       

tests/test_game_logic.py ......                                   [100%]

=========================== 6 passed in 0.02s ===========================
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
