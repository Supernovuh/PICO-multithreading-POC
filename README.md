# Multithreading proof of concept
Code to blink an led until a specified section of code is done completing in another thread


proof of concept - this solves a basically nonexistent issue - proves the use of two threads on a raspberry pi pico


How to use

1 - Specify what pin the LED is on - line 13

2 - Set function to run when the PICO gets power - lines 25-26

3 - Set code to run while setup function is running - lines 41-42 (dont edit to leave the LED blinking)

4 - Enter main code - line 48
