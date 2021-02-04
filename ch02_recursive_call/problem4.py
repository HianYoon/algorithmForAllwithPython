# 4-1
def sum_from_one_to_n(n):
    if n == 1:
        return 1
    return n + sum_from_one_to_n(n-1)


print(f"4-1의 답은 {sum_from_one_to_n(3)}")

# 4-2 파라미터 미 사용 시
a = [3, 1, 2, -1, 5, 99, 4]
# max_num = 0
#
#
# def find_max(n):
#     global max_num
#     if n == len(a):
#         return max_num
#
#     if max_num < a[n]:
#         max_num = a[n]
#
#     find_max(n+1)
#     return max_num
#
#
# def first_def(param):
#     global max_num
#     max_num = param[0]
#     print(find_max(0))
#
#
# first_def(a)
# print(max_num)
##########################################
#파라미터 사용 시


def find_max(a):
    max_num = a[0]

    def max_cal(n):
        nonlocal max_num
        if n == len(a):
            return
        if a[n] > max_num:
            max_num = a[n]
        max_cal(n + 1)

    max_cal(0)

    return max_num


print(find_max(a))
