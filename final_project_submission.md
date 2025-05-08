
# Final Project Feature Submission

## 1. Define Your Objective

For my final iteration, I wanted to make my game feel more interactive and visually polished. I chose to implement **two features**:
- A friendly NPC in the town square that gives the player a potion the first time they visit.
- A graphical combat system using Pygame to replace the previous text-based one.

Both features were small enough to complete in a week but added meaningful improvements to the game.

---

## 2. Set Goals & Plan Your Work

**Goal 1:** Display a text-based NPC interaction when entering the town tile (0, 0).  
**Goal 2:** Give the player one free potion from the NPC — only once.  
**Goal 3:** Replace the old combat function with a Pygame-based graphical combat window.  
**Goal 4:** Keep everything working with existing systems (inventory, map, monsters, etc).

---

## 3. Implement Your Feature

Both features were added and tested:
- The NPC appears in the terminal when you enter the town for the first time. The player receives one potion. After that, the NPC gives a different message but no more potions.
- Combat now opens a separate Pygame window. The player and monster appear as rectangles, and HP is shown. Pressing "A" lets the player attack. Messages appear for hits and kills.

I used version control throughout and tested all interactions with the map and menu.

---

## 4. Self-Evaluation & Reflection

**What went well:**  
The NPC interaction was really easy to add once I figured out how to track if the player had already talked to them. The graphical combat was fun to code and worked on the first try.

**What challenges did you face?**  
The hardest part was making sure the NPC only gave the item once and making sure the graphical combat window didn’t crash the game after ending.

**How did you overcome them?**  
I added a flag called `npc_interacted` and used it to check if the player had already visited. For combat, I used the Pygame event loop and added clean exit conditions to go back to the map.

**If you had more time, what would you improve?**  
I would add sprites for the player and monster, a health bar instead of numbers, and maybe attack animations or sound effects.

