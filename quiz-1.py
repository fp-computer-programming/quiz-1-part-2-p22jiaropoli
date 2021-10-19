# Author JRI 10/19/21

# input statements

year = int(input("enter the year of the date "))
m = int(input("enter the month of the date as an integer "))
q = int(input("enter the day of the date "))

j = year // 100
k = year % 100

# conditionals

if m == 1 or m == 2:
    m += 12
    year = year - 1

# equation

h = (q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7

# print statement

if h == 0:
    h = str("Saturday")
elif h == 1:
    h = str("Sunday")
elif h == 2:
    h = str("Monday")
elif h == 3:
    h = str("Tuesday")
elif h == 4:
    h = str("Wednesday")
elif h == 5:
    h = str("Thursday")
elif h == 6:
    h = str("Friday")


print("The date was a " + h)
