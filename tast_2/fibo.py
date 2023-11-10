# Fibonacci Generator by a mathematical recurrence relationship.

def fibo(n):
    if n==0:
        return 0
    elif (n==1):
        return 1

    else:
        return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print(f"Using recursions value of fib({num}) is {fibo(num)}")
