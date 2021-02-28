# 답 안보고 푼 버전
def search_fake_coin(li, left, right):
    # if only one index is left to be checked, it means it is the fake coin
    if right - left <= 0:
        return left
    left_value = li[left]
    right_value = li[right]

    if left_value != right_value:
        return left if left_value < right_value else right
    else:
        return search_fake_coin(li, left+1, right-1)


ex = [3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3]
answer = search_fake_coin(ex, 0, len(ex) - 1)
print("답 안보고 만든 솔루션", answer)


# ####################################################
# solution 1
def weigh(a, b, c, d):
    fake = 29
    if a <= fake <= b:
        return -1
    if c <= fake <= d:
        return 1
    return 0


def edited_first_solution(left, right):
    # termination condition
    if right - left <= 0:
        return "There is no fake coin."

    result = weigh(left, left, right, right)
    if result == -1:
        return left
    elif result == 1:
        return right
    else:
        return edited_first_solution(left + 1, right - 1)


n = 100
print("\n첫 번째 방법 효율적으로 변경. \n책에 써져있는 방법에 비해 최악의 경우가 n/2으로 감소", edited_first_solution(0, n - 1))


# ####################################
def second_solution(left, right):
    # termination condition
    if left == right:
        return left
    target1_left = left
    target2_left = (right + left) // 2 + 1
    target2_right = right
    target1_right = right - target2_left + target1_left
    result = weigh(target1_left, target1_right, target2_left, target2_right)
    if result == 0:
        return target2_left - 1
    elif result == -1:
        return second_solution(target1_left, target1_right)
    else:
        return second_solution(target2_left, target2_right)


n = 50
print("두번째 방법", second_solution(0, n - 1))
