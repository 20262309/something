numbers = []
for i in range(9):
    n = int(input())
    numbers.append(n)

max_value = numbers[0]
max_index = 0

for i in range(9):
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i

print(max_value)
print(max_index + 1)