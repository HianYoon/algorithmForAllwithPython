# 8-1
def select_sort(li):
    length = len(li)
    for i in range(0, length - 1):
        min_index = i
        for k in range(i+1, length):
            if li[min_index] > li[k]:
                min_index = k
        li[i], li[min_index] = li[min_index], li[i]


ex = [2, 4, 5, 1, 3]
select_sort(ex)
print(ex)