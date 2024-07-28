def add_numbers(n):
    return sum(int(input()) for _ in range(n))

def subtract_numbers(n):
    result = int(input())
    for _ in range(n-1):
        result -= int(input())
    return result

n = int(input("Enter the number of elements: "))
if n > 0:
    operation = input("Enter operation (add or subtract): ").strip().lower()
    
    if operation == "add":
        print(add_numbers(n))
    elif operation == "subtract":
        print(subtract_numbers(n))
    else:
        print("Invalid operation")
