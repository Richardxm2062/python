def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib_sequence = fibonacci(n)
    print(f"The first {n} Fibonacci numbers are:")
    print(fib_sequence)

if __name__ == "__main__":
    main()
