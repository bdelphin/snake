# Snake Game for RPi SenseHat
Classic Snake Game designed for the Raspberry Pi SenseHat. 

Two versions available : one built with Scratch2, the other one with Python. 
Developed by Baptiste DELPHIN (baptiste.delphin@gmail.com)

## Instructions : Scratch2 version
Simply open the Scratch Project (.sb2 file) with Scratch2.
Enable turbo mode and run the project (or hold Shift & click Run).

## Instructions : Python version 
SenseHat Python module is needed, simply install it with:
```
sudo apt-get install sense-hat
```
Plug the SenseHat, power your Pi back on, and simply launch:
 ```
python snake.py
```

## About
It was initialy built with Scratch2 for testing purposes (I've always wanted to try it, but  never found the time before).
Disappointed with Scratch2 latency (even in turbo mode), I decided to remake the game with Python. Much faster it is.

Feel free to improve the code if you wish, I'm not a Python guru and this was built in a really short time.

## Game display & controls
The game is displayed on the LED matrix, you can control the snake with the tiny joystick.

Highscore is stored in .snake file (except for the Scratch version which lacks that functionality for now. Maybe I'll implement it later)

If you encounter any issue feel free to contact me via email.
