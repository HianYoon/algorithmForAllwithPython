ex = [4, 5, 3, 2, 6, 9]


def find_min_num(li):
    # parameter가 list가 아니면
    if not isinstance(li, list):
        print("System : Error  - 입력된 값이 리스트 타입이 아닙니다.")
        return

    # parameter가 list이면
    min_num = li[0]
    # 0번 인덱스를 비교할 필요가 없으므로 range 함수를 썼습니다.
    # 원래는 range 대신 li를 넣어도 되겠지만... 0번 인덱스..딱 한 개 더 하는 거긴 한데... 뭐 솔직히 별거 아니죠... ㅋㅋ
    for i in range(1,len(li)):
        if min_num > li[i]:
            min_num = li[i]
    return min_num


print(find_min_num(ex))

