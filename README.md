# Alien Invasion

## Overview of files

### alien_invasion.py
- This contains the AlienInvasion class
- This creates many important attributes, such as settings, screen, and ship
- The main loop of the game is also stored here, which runs check_events() and update_screen()
- The check_events() method detects relevant results, such as keypresses and key releases
- The update_screen() method redraws the screen on each pass through the loop

### settings.py
- This contains the Settings class
- Only has an init() method, which initializes attrubites like game appearnce and ship speed

### ship.py
- This contains the Ship class
- The update() method manages the ship's position
- The blitme() method draws the ship to the screen
