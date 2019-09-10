import itertools
fd = open("""Resources/Day_04.txt""", 'r')
#open('Resources/Day_04.txt').read().split('\n')
src = fd.read()
lines = src.split('\n')

class Event:
    def __init__(self, ts, action, guard = 0):
        self.ts = ts
        self.action = action
        self.guard = int(guard)
                
    def __repr__(self):
        return "ts: %s action: %s guard: %s" % (self.ts, self.action, self.guard)

#first parse input, and sort the log
log = []
sleepLog = dict()
for each in lines:

    parts = each.split()
    ts = parts[0] + ' ' + parts[1]
    txt = parts[2]
    guardId = 0

    # falls asleep
    if txt == 'falls':
        action = 0;
    #wake up
    elif txt == 'wakes':
        action = 1
    #new guard
    else:
        action = 2
        guardId = parts[3][1:]
        sleepLog[int(guardId)] = [0 for x in range(60)]

    log.append(Event(ts, action, guardId))

log.sort(key=lambda x: x.ts)

#part 1 - calculate sleep minutes
activeGuard = 0
minute = 0
for each in log:
    if each.action == 2:
        activeGuard = each.guard
        #part 1 doesn't care, when he starts his shift
        continue

    #fall asleep
    if each.action == 0:
        minute = int(each.ts.split(':')[1][:-1])

    # wake up
    if each.action == 1:
        minuteEnd = int(each.ts.split(':')[1][:-1])
        #log it
        for m in range(minute, minuteEnd):
            sleepLog[activeGuard][m]+= 1
    
longestSleeper = max(map(lambda x: sum(x), sleepLog.values()))
frequentMinute = max(m for l in sleepLog.values() for m in l)
for guard, sleep in sleepLog.items():
    if sum(sleep) == longestSleeper:
        longestMinute = sleep.index(max(sleep))
        print("Lazy: " + str(guard) + " in " + str(longestMinute) + " minute -> " + str(guard*longestMinute))

    if frequentMinute in sleep:
        frequentMinuteIdx = sleep.index(frequentMinute)
        print("Freq: " + str(guard) + " in " + str(frequentMinuteIdx) + " minute -> " + str(guard*frequentMinuteIdx))
