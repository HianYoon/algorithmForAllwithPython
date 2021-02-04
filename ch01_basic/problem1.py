# 1-1
def sum_of_square(n) :
    total = 0
    for i in range(1, n+1):
        total += i * i
    print(f"1부터 {n}까지의 제곱수들의 합은 {total}")


sum_of_square(3)