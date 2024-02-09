def knapSack(bag_weight, item_weights, item_prices, items_count):
    if items_count == 0 or bag_weight == 0:
        return 0

    if item_weights[items_count - 1] > bag_weight:
        return knapSack(bag_weight, item_weights, item_prices, items_count - 1)

    else:
        return max(
            item_prices[items_count - 1]
            + knapSack(
                bag_weight - item_weights[items_count - 1],
                item_weights,
                item_prices,
                items_count - 1,
            ),
            knapSack(bag_weight, item_weights, item_prices, items_count - 1),
        )


# value = [60, 100, 120]
# weight = [10, 20, 30]

value = [120, 100, 60]
weight = [30, 20, 10]
capacity = 50
n = len(value)
print(knapSack(capacity, weight, value, n))
