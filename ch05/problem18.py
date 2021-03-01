def search_maximum_profit(li):
    current_maximum_profit = 0
    minimum_price = li[0]

    for i in range(1, len(li)):
        current_price = li[i]
        current_profit = current_price - minimum_price
        if current_maximum_profit < current_profit:
            current_maximum_profit = current_profit
        if minimum_price > current_price:
            minimum_price = current_price
    return current_maximum_profit


ex = [2, 2, 0, 4, 5, 6, 7]
print(search_maximum_profit(ex))
