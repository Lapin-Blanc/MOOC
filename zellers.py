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

month_name = raw_input("Month: ").lower()
while month_name not in months:
    month_name = raw_input("Please enter a valid month name: ")
A = months.index(month_name)+1
# TODO check day value
B = input("Day: ")
# TODO check year value
C = input("Year: ")
if A in [11,12]:
    C -= 1
# TODO check year value
D = input("Century: ")
if C == -1:
    D -= 1
    C = 99
# print A, B, C, D
# Algorith following homework
W = (13*A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z%7

print days[R], month_name, B, str(D)+str(C)
