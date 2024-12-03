
import re
f = open('3.txt', 'r')
d={
    '-': 'минус',
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
}
s = f.readline().split()
while s!=[]:
    for i in s:
        match = re.match(r"^-?[01234567]+$", i)
        if match and int(i,8)<=4096:
            if ((len(i)%2==0 and '-' not in i) or ((len(i)-1)%2==0 and '-' in i)) and int(i)%2==0:
                for sym in i:
                    if sym!='-': print(d[sym], end = ' ')
                print()
            else: print(i)     
    s = f.readline().split()