# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
-bug documentation 
#1 the hint was ineffective. I expected it to accurately tell me high or low but it simply kept saying low till i ran out of attempts
#2 ran out of attempts before i had went 8 times
#3 pop ups dont close when a new game is started or when the ui is updated in general

- What did the game look like the first time you ran it?
  text based game with no background asking me to guess the secret number
- List at least two concrete bugs you noticed at the start  
  the hint for go lower or higher was broken as the first guess i had was much lower than the secret but the hint kept telling me to go even lower 
  Also the attempt tracker isnt accurate 
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

first user prompt to AI - ive written a few comments that show some bug locations within the code go over the first one with difficulty slider within the app.py file (ive already changed the difficulty point parameter just change it in the rest of the code logic so that it flows smoothly and properly cordinates with the desired difficulty)

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The Ai suggested  line of code to bad added that simply caused another error in the hint bar when ran


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
ran the code and tested the function i was working on to see if it was working within my expectations
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  started the code and checked the difficulty sliders and how they affected my attempt number and score. Upon realising that the difficultys were mismatched i attempted to have the ai correct it but it made it worse so i rewrote it by hand then rechecked to see if the slider made sense. from their i realised another logic problem within the score calculation that i had the ai fix.
- Did AI help you design or understand any tests? How?
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing in the original app because it was being regenerated every time Streamlit reran the script, which happens on every user interaction like submitting a guess. This meant that even if the player guessed correctly, the secret would change before the app could check it, making it impossible to win. Without proper session state management, the app treated each rerun as a fresh start, losing the previous secret.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns are like refreshing the entire app every time something changes, such as when you click a button or enter text, so the code runs from top to bottom again to update the display. Session state is like a persistent memory that saves data across these reruns, so things like your score or the secret number don't get wiped out each time the app refreshes. It's what keeps the game feeling continuous, even though the code is re-executing constantly.

- What change did you make that finally gave the game a stable secret number?
I changed the initialization logic in app.py to only generate a new secret when the user explicitly starts a new game or changes the difficulty level, instead of regenerating it on every rerun. This was done by moving the secret generation into conditional blocks that check for new game or difficulty changes, and ensuring session state is set only once on first load. Additionally, I hid the secret from the debug info to prevent cheating and made sure the logic functions in logic_utils.py handle types properly to avoid unexpected behavior.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I would first like to make a format that I want the ai to follow as well as a list of things i would want it to focus on during the project while leaving task that could break the overall security or stability of the code to myself.
- What is one thing you would do differently next time you work with AI on a coding task?
 only use it on a process that i understand the purpose of 100 percent
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think ai generated code are simply quickly put together code that satisfy the prompt given in the smallest capacity possible. It is evident that it will likely not fully flesh out your wishes on its own as its understanding of our wishes is inadequate no matter how in depth our explanation is.
