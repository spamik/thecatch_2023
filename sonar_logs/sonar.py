import pytz
import datetime

records = {}
with open('sonar.log', 'r') as f:
    for i in f.readlines():
        dt, tm, tz, rest = i.split(' ', 3)
        zone = pytz.timezone(tz)
        dto = zone.localize(datetime.datetime.strptime(dt + ' ' + tm, '%Y-%m-%d %H:%M:%S'))
        records[dto] = rest

flag = ''
for i in sorted(records.keys()):
    if 'depth' in records[i]:
        a, b, c, d, e, depth, hx = records[i].split(' ')
        flag += chr(int(depth))
print(flag)

