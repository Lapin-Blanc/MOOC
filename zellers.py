# Zellers optionnal homework
# 

months = ["march",
           "april",
           "may",
           "june",
           "july",
           "august",
           "september",
           "october",
           "november",
           "december",
           "january",
           "february"]

days = ["sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"]

# Input a year of the gregorian calendar
# loop while input is invalid
year = input("Year: ")
while year<1582:
    year = input("Enter a year of the gregorian calendar (>=1582): ")

# Input a month name (ie: january, february, etc.)
# loop while input is invalid
month_name = raw_input("Month name in english: ").lower()
while month_name not in months:
    month_name = raw_input("Please enter a valid month name: ")
A = months.index(month_name)+1
month_num = (A + 1) % 12    # Jan = 0, Feb = 1, ...
# A contains index of month for algorithm
# month_num contains month index as with Jan = 0, Feb = 1, ...


# Input a day number
# loop while input is invalid
# Leap year ?
is_leap = (year%4 == 0) and not ((year%100 == 0) and (year%400 != 0))
# compute number of days in the choosen month
if month_num == 1:          # February
    if is_leap:
        month_days = 29
    else:
        month_days = 28
else:
    month_days = 31 - (month_num % 7 % 2)
B = input("Day: ")
while not((B>0) and (B<=month_days)):
    B = input("Please input a valid day number for this month: ")



# Corrections for algorithm
cyear = year                 # to keep original year to print final result
if A in [11,12]:
    cyear -= 1
C = cyear % 100              # C assigned to year : 89 for 1989, ...
D = cyear // 100             # A assigned to century : 19 for 1989, ...

# Algorith following homework
W = (13*A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z%7

print days[R], month_name, B, year
