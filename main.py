from threading import Thread
import random
import time


def one_thread(poem):
    for x in range(0, len(poem)):
        pos = x
        time.sleep(.3)
        print poem[x]

def anotha_thread(poem):
    global pos
    for y in range(0, len(poem)):
        pos = y
        time.sleep(.2)
        print poem[y]


def main():
    global pos
    t = None

    with open('caged_bird.txt') as f:
        data = f.readlines()

    t1 = Thread(target=one_thread, args=(data,))
    t2 = Thread(target=anotha_thread, args=(data,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
