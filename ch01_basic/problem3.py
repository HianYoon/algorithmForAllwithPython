ex = ["Hian", "굴공", "Py", "쿠우"]


def calculate_every_match(li):
    if not isinstance(li, list):
        print("입력 값이 리스트가 아닙니다")
        return
    result = set()
    for i in range(0, len(li)):
        for k in range(i+1, len(li)):
            result.add(frozenset([li[i], li[k]]))
    return result


print(calculate_every_match(ex))


