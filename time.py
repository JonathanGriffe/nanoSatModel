from math import floor

LOG_FILE = "SCI_Coverage_Log_v1.4.txt"
logf = open(LOG_FILE, "r")
logs = logf.readlines()
logf.close()

obs = [0,0,0,0,0,0,0,0,0,0]
minObs = 0

for line in logs:
    star = int(line[29:31])
    state = line[53:]
    print(obs)
    if state == 'ok\n':
        obs[star - 1] += 1
        if min(obs) > minObs:
            minObs += 1
            date = float(line[38:50]) - 60126
            logDay = floor(date)
            logSecond = date % 1 * 86400
            print(f"Number of obs : {minObs} reached at date {logDay} {logSecond}")
