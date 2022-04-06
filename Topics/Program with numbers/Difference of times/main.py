# put your python code here
time1 = {'h': 0, 'm': 0, 's': 0}
time2 = {'h': 0, 'm': 0, 's': 0}

for key, value in time1.items():
    time1[key] = input()

for key, value in time2.items():
    time2[key] = input()

timediff = {}

for key, value in time2.items():
    timediff.update({key: (int(time2[key])-int(time1[key]))})

print(3600*timediff['h'] + 60 * timediff['m'] + timediff['s'])
