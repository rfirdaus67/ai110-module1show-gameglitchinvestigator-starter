# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The hints were backwards; When the number is higher, the hint is "Go HIGHER" and vice versa
- "New Game" button doesn't start a new game; Must reload the page to restart
- "Attempts left" starts 1 less than it should (7 instead of 8 for Normal); Attempts starts at 1 instead of 0
- Range for "Easy" should be 1-20 but the secret number is out of this range and the text still says 1-100
- Range for "Easy" should be 1-50 but the secret number is out of this range and the text still says 1-100
- When the guess isn't a number, the "Attempts left" still decreases and can go below 0
- After the first guess, "Attempts left" did not decrement 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
   50         Go LOWER!          Go HIGHER!              none
   "W"    "Attempts left" to     "Attempts left"         none
          remain the same        decreases
   20      Secret number        Secret number is         none
        should be between 1-20. outside this range
            for easy mode
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used both Claude and ChatGPT for help. One issue I had to fix was the "Attempts Left" section not decrementing after the first guess. AI suggested i use st.rerun to reload the page after the guess and I verified this by running the program and seeing if the display decremented after submitting my first guess. An AI suggestion that was misleading was after the st.rerun line, my hints were no longer showng up. It seemed there wasn't a simple fix to get both working and I needed to change multiple lines of code. ChatGPT suggested I restructure the submit block and make a new session state variable for the hint, so I didn't have to use st.rerun, but this was incorrect. I checked this because I would either get an error, the hints were not showing up or the "Attempts Left" wasn't decrementing after the first guess. When I asked Claude, it turned out I needed to use a combination of these things to get my program working.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was fixed by testing it multiple times, with different inputs and if the program was reloaded/rerun, to make sure it would work multiple times and in certain situations. One test I ran was the test_new_game using pytest that Claude helped me design. This helped me understand the changes Claude made better because in order for a new game to start and not get stuck, the conditions at the end of the game (status, history, etc.) needed to match the conditions for a new game. Unless the history was cleared and the attempts were at 0 for example, the "New Game" wouldn't work.

## 4. What did you learn about Streamlit and state?

- I learned that in Streamlit, st.rerun essentially runs the script over again and stops its current execution. Since variables are recreated on each rerun, the session state saves information between reruns. For example, when the user is making their guess attempts, then the session state saves the attempt number the user is on even with rerunning the program. 


## 5. Looking ahead: your developer habits

- One habit I want to reuse is testing changes and documenting these changes with comments that explain what the issue was and what was fixed. By testing after each change, I can isolate bugs and if I'm getting code from somewhere else to fix these bugs, I can understand what caused them and what fixed them. Another goal of mine is to commit my chnages using Git more often. This way I can save my progress and fix sections of my code with one concise message rather than saving at the end and having to write all my changes.

- One thing I would do differently is try using more Ai agents to see how their suggestions differ. This way I can also see if they produce similar results and can use this since it seems to be more common. I would also use more persona prompting such as telling Ai to "act like a Python developer." That way, the Ai can better understand my perspective and give more specific outputs based on how I would think or approach a bug.

- This project showed me that code generated by Ai can be helpful for speeding up the process, especially for debugging, but it's not always right. It's important for the developer to double check the code and sometimes, to even debug what Ai gives you to find a solution.
