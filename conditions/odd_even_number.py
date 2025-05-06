def main():
    n = int(input("Enter the number: "))
    
    if is_even(n):
        print(f" Number {n} is even")
    else:
        print(f" Number {n} is odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         False

# def is_even(n):
#     return True if n % 2 == 0 else False 

def is_even(n):
    return n % 2 == 0

main()