#!/usr/bin/env python3
import threading
import time
import sys
import os
from os.path import expanduser
from pathlib import Path
from datetime import date
import json

# paused atomic, 0 is go, 1 is paused, -1 is stop, -2 is stopped
pAtomic = 0
pLock = threading.Lock()
appDir = expanduser("~/.local/share/pytimer")
timeTXT = f"{appDir}/time.txt"

today = date.today().strftime("%d")
Path(appDir).mkdir(parents=True, exist_ok=True)
if not os.path.exists(timeTXT):
    with open(timeTXT, "w+") as f:
        data = {"day": today, "duration": 0}
        json.dump(data, f, ensure_ascii=False, indent=4)


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
        self.todayDuration = 0
        self.readTime()

    def __str__(self):
        seconds = int(time.time() - self.start - self.pausedDuration)
        s = seconds % 60
        m = seconds // 60 % 60
        h = seconds // 3600
        return "{:02}:{:02}:{:02}".format(h, m, s)

    def timer(self):
        p = getAtomic()
        # quit
        if p == -1:
            self.calcPaused()
            print("\nFinal Time: {}".format(self.finalTime()))
            print("Time Today: {}".format(self.timeToday()))
            self.writeTime()
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

    def finalTime(self):
        seconds = int(time.time() - self.start - self.pausedDuration)
        m = seconds // 60 % 60 * 5 // 3
        h = seconds // 3600
        return "{}.{:02}hrs".format(h, m)

    def timeToday(self):
        seconds = int(time.time() - self.start - self.pausedDuration)
        self.todayDuration += seconds
        seconds = self.todayDuration
        m = seconds // 60 % 60 * 5 // 3
        h = seconds // 3600
        return "{}.{:02}hrs".format(h, m)

    def calcPaused(self):
        if self.lastPaused != 0:
            self.pausedDuration += time.time() - self.lastPaused
            self.lastPaused = 0

    def readTime(self):
        with open(timeTXT, "r+", encoding='utf-8') as f:
            data = json.load(f, encoding='utf-8')
            if data["day"] != today:
                data = {"day": today, "duration": 0}
            self.todayDuration = data["duration"]

    def writeTime(self):
        with open(timeTXT, "w") as f:
            data = {"day": today, "duration": self.todayDuration}
            json.dump(data, f, ensure_ascii=False, indent=4)


def runThread():
    s = Stopwatch()
    while getAtomic != -2:
        s.timer()
        time.sleep(1)


def run():
    t = threading.Thread(target=runThread)
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
