import threading
import time
import sys
import os

# paused atomic, 0 is go, 1 is paused, -1 is stop, -2 is stopped
pAtomic = 0
pLock = threading.Lock()


def swapAtomic(stop=False, stopped=False):
    global pAtomic
    pLock.acquire()
    if stop:
        pAtomic = -1
    elif stopped:
        pAtomic = -2
    else:
        pAtomic = (pAtomic + 1) % 2
    pLock.release()


def getAtomic():
    global pAtomic
    pLock.acquire()
    p = pAtomic
    pLock.release()
    return p


class Stopwatch:

    def __init__(self):
        self.start = time.time()
        self.lastPaused = 0
        self.pausedDuration = 0

    def __str__(self):
        seconds = int(time.time() - self.start - self.pausedDuration)
        s = seconds % 60
        m = seconds // 60
        h = seconds // 360
        return "{:02}:{:02}:{:02}".format(h, m, s)

    def timer(self):
        p = getAtomic()
        # quit
        if p == -1:
            self.calcPaused()
            print("\nFinal Time: {}".format(str(self)))
            swapAtomic(stopped=True)
            return
        # not paused
        elif p == 0:
            self.calcPaused()
            print(str(self))
        # paused
        else:
            if self.lastPaused == 0:
                self.lastPaused = time.time()
                print("paused")
        time.sleep(1)
        self.timer()

    def calcPaused(self):
        if self.lastPaused != 0:
            self.pausedDuration += time.time() - self.lastPaused
            self.lastPaused = 0


def run():
    s = Stopwatch()
    t = threading.Thread(target=s.timer)
    t.start()
    while 1:
        input()
        swapAtomic()


try:
    run()
except KeyboardInterrupt:
    swapAtomic(stop=True)
    while getAtomic() != -2:
        pass
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
