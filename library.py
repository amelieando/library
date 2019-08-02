from turtle import *
color('blue', 'pink')
begin_fill()
while True:
    forward(100)
    left(45)
    if abs(pos()) < 1:
        break
end_fill()
done()

import calendar
calendar.setfirstweekday(calendar.FRIDAY)
calendar = calendar.calendar(2019, w=2, l=1, c=6, m=3)
print(calendar)

import math
math1 = math.copysign(-3,2)
print(math1)

math2 = math.fabs(-4)
print(math2)

math3 = math.factorial(4)
print(math3)

math4 = math.ceil(3.0)
print(math4)

math5 = math.floor(3.9)
print(math5)
