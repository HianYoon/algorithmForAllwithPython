# 15-1
ex = {
    1: [2, 3],
    2: [1, 2, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}


def graph_traverse(dic, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        for x in dic[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
    print(done)


graph_traverse(ex, 1)