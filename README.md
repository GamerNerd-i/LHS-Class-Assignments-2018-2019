# LHS-Class-Assignments-2018-2019
## Contents

### Notes
Notes taken during class, shows what the lessons were.

### Dionisio, Aidan
The actual programming assignments, split up further into folders.
* Each folder (Programming Assignment #) might have a few different programs and other stuff, like what my teacher used for testing or necessary files for the assignment, such as Programming Assignment 6 having graphics.py.

### Project: Event Horizon AI
Sometimes had too much free time during class to finish the assignments, so I started a little thing for fun and promptly forgot about it. But it's still there. Event Horizon is basically an RPG with friends I've been trying to make, and since I didn't really want to be the enemy CPU I was trying to write one to do it for me. The game plays like Fire Emblem, so I was trying to integrate those mechanics first. All programs incomplete.
* weapons: Listing weapons and attributes; color (Red, Green, Blue), type (Physical, Energy), and effectiveness (based on movement type or other factors). Intended to be imported for use into other programs that would actually use the data.
* EHDuels: Intended for use with battle_functions. Inputs for stats/attributes for the Initiator and Defender, calculates damage based on stats and weapon attributes (phsyical/energy and the rock-paper-scissors weapon triangle), and checks when someone dies.
* EHBattleAI: Tentative setup for the map, before duels can happen. Takes down map size (x/y), unit positions, unit movement, unit deaths, and checks for victory conditions (currently only for "eliminate all enemies")
* battle_functions: Actual execution of duels using the code from EHDuels. Calculates damage and initiates the fights. Not intended to go to the death, but that's what it does now. Includes dictionaries of combatants for testing. Last I checked, didn't work as intended.
