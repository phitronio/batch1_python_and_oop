# odd number ==> after dividing by 2, the remainder will be 1
# even number ==> after dividing by 2, the remainder will be 0
from tkinter import N


num = 7
while num <= 20:
    num = num + 1
    if num % 2 == 1:
        continue
    print(num)
