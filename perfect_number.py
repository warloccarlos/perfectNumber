class perfect:
    def number():
        n = int(input("Enter a number: "))
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        if sum == n:
            print(f"{n} is a perfect number")
        else:
            print(f"{n} is not a perfect number")

if __name__ == "__main__":
    while True:
        perfect.number()
        cont = input("Do you want to check another number? (yes/no): ").strip().lower()
        if cont != 'yes':
            break