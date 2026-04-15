y = int(input())
if (y % 400 == 0) or ((y % 4 ==0) and (not(y % 100 == 0))):
    print ("%d is a leap year" %y)
else:
    print ("%d is not a leap year" %y)