from msvcrt import getch
import threading
import random
import time
import sys


lock = threading.Lock()

def thread(poem):
    global pos
    
    while (pos < count):
        lock.acquire()
        pause()
        pos += 1
        pos = pos_reset(pos)
        
        time.sleep(.2)
        lock.release()    

def thread2(poem):
    global pos
    while (pos < count):
        lock.acquire()
        pause()
        if (pos < count):
            print poem[pos]

        time.sleep(.2)
        lock.release()

def thread3(poem):
    global key, ay
    luck = threading.Lock()
    while keysearch == True:
        with luck:
            key = getch()
            if (ay==True):
                ay = False
    
def pos_reset(n):
    if (n == count):
        return 0
    else:
        return n

def pause():
    global key, ay, pos, keysearch
    
    cv.acquire()
    if (key=="1"):
        print "\nPAUSING THREADS..."
        secs = random.randint(1, 4)
        time.sleep(secs)
        ay = True

        informed=False
        while ay == True:
            cv.wait(.1)
            if informed == False:
                print "\nPAUSED\n\nPRESS ANY KEY TO RESUME...\n"
                informed = True
            
        cv.notifyAll()
        cv.release()
        key =4
        
    elif (key=="2"):
        print '---PRESS ANY KEY TO CLOSE PROGRAM---'
        pos = count
        keysearch = False
        time.sleep(.5)
        cv.notifyAll()
        cv.release()
        key = 4
        
    else:
        cv.notifyAll()
        cv.release()

def main():
    global pos, count, key, cv, ay, keysearch
    
    key = "lol"
    play = True
    pos = -1
    keysearch =True

    with open('caged_bird.txt') as f:
        data = f.readlines()
    
    count = len(data)

    cv = threading.Condition()
    ay = False
    t1 = threading.Thread(target=thread, args=(data,))
    t2 = threading.Thread(target=thread2, args=(data,))
    t3 = threading.Thread(target=thread3, args = (data,))

    t1.start()
    t2.start()
    t3.start()
 
    
    t1.join()
    t2.join()
    t3.join()
    

if __name__ == '__main__':
    main()
