def main():
    number = get_number()
    meow(number)

def get_number():
    n = int(input("Enter number gt 0: "))
    while True:
        if n > 0:
            return n 
        
def meow(n):
    for _ in range(n):
        print("meow")
        
main()