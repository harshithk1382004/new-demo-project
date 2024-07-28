def add_numbers(n):
    return sum(int(input()) for _ in range(n))

n = int(input())
if n > 0:
    print(add_numbers(n))
