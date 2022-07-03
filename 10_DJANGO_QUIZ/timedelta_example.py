import datetime


def sec2str(seconds):
    return datetime.datetime.fromtimestamp(seconds)


start = datetime.datetime(2022, 2, 12, 4, 56, 23, 345)
end = datetime.datetime(2022, 5, 23, 12, 3, 43, 234)


sec1 = round((end - start).total_seconds())
sec2 = round((end - start).total_seconds())

td = end - start
print(f'td to repr >> {td!r}')
print(f'td to str >> {td!s}')
print(f'td to ascii >> {td!a}')
print(f'td.days = {td.days}')
print(f'td.seconds = {td.seconds}')
print(f'td.microseconds = {td.microseconds}')
print(f'td.resolution = {td.resolution}')
print(f'td.min = {td.min}')
print(f'td.max = {td.max}')

print(f'sec1 = {sec1}, sec2 = {sec2}')

# sec1 = 25639

d = sec1 // 86400
sec1 -= d * 86400
h = sec1 // 3600
sec1 -= h * 3600
m = sec1 // 60
s = sec1 - m * 60


print(sec2str(sec2))
print(f'{d:02} {h:02}:{m:02}:{s:02}')
