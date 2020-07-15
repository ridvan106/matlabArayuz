import threading
import time
def printName(threadName,value):
    while(True):
        print(threadName,value);
        time.sleep(1)


threading._start_new_thread(printName,('Aleyna',10));
threading._start_new_thread(printName,('Ridvan',5));

while(True):
    time.sleep(1)