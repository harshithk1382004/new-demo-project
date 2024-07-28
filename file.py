def add_numbers(n):
    total = 0
    for _ in range(n):
        total += int(input())
    return total

n = int(input())
if n > 0:
    print(add_numbers(n))
