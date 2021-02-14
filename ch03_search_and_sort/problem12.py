# 12-1
def binary_search(li, value, start, end):
    # 조건 1
    if end - start <= 0:
        return -1

    mid = (start + end) // 2

    if value == li[mid]:
        return mid
    elif value > li[mid]:
        start = mid + 1
    else:
        end = mid - 1

    return binary_search(li, value, start, end)


def quick_sort_function(li, start, end):
    if end - start <= 0:
        return
    pivot = li[end]
    i = start
    for j in range(start, end):
        if li[j] <= pivot:
            li[i], li[j] = li[j], li[i]
            i += 1
    li[end], li[i] = li[i], li[end]
    quick_sort_function(li, start, i - 1)
    quick_sort_function(li, i + 1, end)


def quick_sort(li):
    quick_sort_function(li, 0, len(li)-1)


def start_function(li, value):
    quick_sort(li)
    return binary_search(li, value, 0, len(li) - 1)


ex = [3,5,7,2,1,4,9,-1]
value = 5.5
print(f"새로운 정렬에서의 {value}의 인덱스 :", start_function(ex, value))
print(f"주어진 리스트는 {ex}로 정렬되었습니다.")
