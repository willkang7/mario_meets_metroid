# Mario Meets Metroid
A wild metroid appears! What will mario do?

## Overview of files

### alien_invasion.py
- This contains the AlienInvasion class
- This creates many important attributes, such as settings, screen, and mario
- The main loop of the game is also stored here, which runs check_events() and update_screen()
- The check_events() method detects relevant results, such as keypresses and key releases
- The update_screen() method redraws the screen on each pass through the loop

### settings.py
- This contains the Settings class
- Only has an init() method, which initializes attrubites like game appearnce and mario speed

### mario.py
- This contains the Mario class
- The update() method manages mario's position
- The blitme() method draws mario to the screen

### bullet.py
- This contains the Bullet class
- The update() method manages the bullet's position
- The draw_bullet() method draws the bullet to the screen
