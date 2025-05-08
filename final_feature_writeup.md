
# Final Feature Write-Up

## Objective & Goals

For my final feature, I wanted to add an NPC (non-player character) that gives the player a free potion when they visit the town. This would make the town square more interactive and give the player something useful early in the game.

Here were my main goals:
1. When the player steps on the town tile (0, 0), a message should appear showing the NPC interaction.
2. The NPC should only give the player a potion the first time they visit.
3. The feature should not break or interfere with the rest of the game.
4. Everything should still work with the map, combat, and inventory system.

---

## What I Accomplished

I added a function to the map code so that when the player walks into the town square, an NPC gives them a potion. I made sure that this only happens once by using a flag that checks if the player already talked to the NPC. If they visit again, the NPC just says something else, and they don’t get another potion.

I also made sure that this new feature didn’t mess with the map, monsters, or player movement. Everything still works like it should — the map loads, monsters move, and the town square heals the player like before.

---

## Self-Evaluation

**What went well:**  
The NPC feature was pretty easy to add once I figured out where to put the interaction. It worked right away and felt like a natural part of the game.

**What challenges did you face?**  
At first, I wasn’t sure how to make the NPC only give the potion once. I had to figure out a way to track that without it resetting every time the player entered the map.

**How did you overcome them?**  
I added a variable that keeps track of whether the NPC already gave the potion. Once it’s set to true, the gift can’t happen again. That solved it.

**If you had more time, what would you improve?**  
I would add graphics or an actual character on the screen for the NPC instead of just using terminal text. I’d also maybe let the NPC offer a choice or two.

