a = int(input())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["일", "월", "화", "수", "목", "금", "토"]

jan = 4

if a<1 or a>12:
    print("not a month")
else:
        total = 0
for i in range (a - 1):
        total += month[i]    
start = (jan + total) % 7
    
print("            ",(str(a) + "월"))
for day in week:
        print(f"{day:>3}", end="")
print()
for i in range(start):
        print("    ", end="")
        
for day in range(1, month[a - 1] + 1):
        print(f"{day:>3}", end=" ")
        
        if (start + day) % 7 == 0:
            print()