#imports
from machine import Pin
import time
import _thread

#this code contains debug messages, such as this. All print statements are not needed, but notify the shell when parts of the code run
print("on...") 

#important setup, dont change
global led

#sets the LED pin. Edit for your needs
ledPin = 25                              #led pin value, 25 on pi pico, edit for other boards

#more setup, do not edit
led = Pin(ledPin, Pin.OUT)
setupStatus = 0
lock = _thread.allocate_lock()

#function to run on second thread
print("starting thread...")
def thread2():
    global setupStatus     #setup, dont edit
    #start of example code, edit as needed
    print("thread started")
    time.sleep(5)
    #end of example code, refrain from editing
    #start of inter-thread communication
    lock.acquire()
    print("writing stop value")
    setupStatus = 1
    lock.release()
    print("end of thread")
    #end of code

#start the code on the thread
_thread.start_new_thread(thread2,())

#code to run while setup is happening, toggles LED, change if you have the need to 
while setupStatus == 0:
    led.toggle()
    time.sleep(.5)

#led on for indicating setup code is done
led.value(1)

#main code here, edit as needed
print("main started")
