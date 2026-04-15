word = input()

total = 0

for w in word:
    if w.islower():
        total += ord(w) - 96
    else:
        total += ord(w) - 38

is_prime = True

for i in range(2, total):
    if total % i == 0:
        is_prime = False

if is_prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")