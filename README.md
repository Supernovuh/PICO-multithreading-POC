# Pico-start-code
Code to notify user when specified 'setup' code has completed by blinking the onboard LED while the code is running and setting it as solid when the main function starts


proof of concept - this solves a basically nonexistent issue - proves the use of two threads on a raspberry pi pico


How to use

1 - Specify what pin the LED is on - line 13

2 - Set function to run when the PICO gets power - lines 25-26

3 - Set code to run while setup function is running - 41-42 (dont edit to leave the LED blinking)

4 - Enter main code - line 48
