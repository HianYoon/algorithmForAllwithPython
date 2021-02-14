# bubble sort
def bubble_sort(li):
    count = 0
    for v in range(0, len(li)-1):
        if li[v] > li[v+1]:
            count += 1
            li[v], li[v+1] = li[v+1], li[v]
    if count != 0:
        bubble_sort(li)


ex = [3, 5, 2, 1, 8, 9]
bubble_sort(ex)
print(ex)
