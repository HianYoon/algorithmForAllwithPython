#9-1
def select_sort(li):
    length = len(li)
    for i in range(1, length):
        value = li[i]
        j = i - 1
        while j >= 0 and value < li[j]: # 9-2 에서는 이 value쪽의 기호만 바꾸면 됨
            li[j+1] = li[j]
            j -= 1
        li[j+1] = value


ex = [2, 4, 5, 1, 3]
select_sort(ex)
print(ex)

