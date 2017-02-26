import time

class Timer:
    def __init__(self, name = "Unnamed", maxTime = 0.0, run = True, startTime = 0.0):
        if startTime == 0:
            startTime = time.time()
        self.startTime = startTime
        self.runTime = 0.0
        self.isRunning = run
        self.name = name
        self.maxTime = maxTime
    
    def Reset(self, run = True):
        self.runTime = 0.0
        self.isRunning = run
        if run:
            self.startTime = time.time()
    
    def Resume(self):
        self.isRunning = True
        self.startTime = time.time()
    
    def Pause(self):
        self.isRunning = False
        self.runTime +=  time.time() - self.startTime
    
    def Toggle(self):
        if self.isRunning:
            self.Pause()
            self.isRunning = False
        else:
            self.Resume()
            self.isRunning = True
        
    def GetTime(self):
        runTime = self.runTime
        if self.isRunning:
            runTime += time.time() - self.startTime
        return runTime
    
    def PrintTime(self):
        runTime = self.GetTime()
        print("%s time: %.4f" % (self.name, runTime))
        
    def IsFinished(self):
        return self.maxTime > 0 and self.GetTime() >= self.maxTime

#testTimer = Timer("stuff")
#time.sleep(1)
#testTimer.PrintTime()

"""
timers = []

def GetTimerHandle(name = "unnamed"):
    for i in range(0, len(timers)):
        if timers[i] == None:
            timers[i] = Timer(time.time(), i, name)
            return i
    handle = len(timers)
    timers.append(Timer(time.time(), handle, name))
    return handle

def GetTimer
"""