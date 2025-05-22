class per_num_range:
    def perf_numbers():
        n = int(input("Enter a number: "))
        perfect_numbers = []
        for i in range(1, n + 1):
            sum = 0
            for j in range(1, i):
                if i % j == 0:
                    sum += j
            if sum == i:
                perfect_numbers.append(i)
        print(f"Perfect numbers up to {n}: {perfect_numbers}")

if __name__ == "__main__":
    per_num_range.perf_numbers()