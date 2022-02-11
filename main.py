#imports
from machine import Pin
import time
import _thread

#print debug message
print("on...") 

#important setup, dont change
global led
#led pin, change
ledPin = 25                 #led pin value, 25 on pi pico, edit 25 for other codes
#more setup, dont changee
led = Pin(ledPin, Pin.OUT)
setupStatus = 0             #0 means setting up, 1 means done with setup, setup status value
lock = _thread.allocate_lock()

#function for second thread
print("starting thread...")
def thread2():
    #setup code for thread, dont change
    global setupStatus
    #example code, change for your purposes
    print("thread started")
    time.sleep(5)
    #end of example code
    #start of inter-thread communication
    lock.acquire()
    print("writing stop value")
    setupStatus = 1
    lock.release()
    print("end of thread")
    #end of code

#start the thread
_thread.start_new_thread(thread2,())

#code to run while setup is happening, toggles LED, change if you have the need to 
while setupStatus == 0:
    led.toggle()
    time.sleep(.5)

#led on for indicating setup code is done
led.value(1)

#main code here
print("main started")