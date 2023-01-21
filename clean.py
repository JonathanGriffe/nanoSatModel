from math import floor

TRANSIT_FILE = "EVTF_TRANSITS_v1.4.txt"
LOG_FILE = "SCI_Coverage_Log_v1.4.txt"
NEW_TRANSIT_FILE = "transits.txt"

transitsf = open(TRANSIT_FILE, "r")
transits = transitsf.readlines()
transitsf.close()

transitsHeader = transits[:22]
transits = transits[22:]

logf = open(LOG_FILE, "r")
logs = logf.readlines()
logf.close()

transitNB = 0

for line in logs:
    date = float(line[38:50])
    state = line[53:]
    if state != 'ok\n':
        logDay = floor(date)
        logSecond = date % 1 * 86400
        transitDay = int(transits[transitNB][0:5])
        transitSecond = float(transits[transitNB][8:20])
        while transitDay != logDay or abs(transitSecond - logSecond) > 0.2:
            transitNB += 1
            transitDay = int(transits[transitNB][0:5])
            transitSecond = float(transits[transitNB][8:20])
        transits.pop(transitNB)

outputf = open(NEW_TRANSIT_FILE, "w")
outputf.writelines(transitsHeader + transits)
outputf.close()
