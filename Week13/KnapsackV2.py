"""Knapsack using dynamic programming"""

import json


def insertionSort(lst: list) -> list:
    """Insertion sorting function by sorted from min value first to max value"""
    for current in range(1, len(lst)):
        hold = lst[current]
        walker = current - 1

        while walker >= 0 and lst[walker][0] > hold[0]:
            lst[walker + 1] = lst[walker]
            walker -= 1

        lst[walker + 1] = hold

    return lst


def knapsack_v2(amount: int, itemList: list):
    """Picking items by using dynamic programming"""
    item_grid = [[0] * amount for _ in range(len(itemList))]
    total = 0

    print(f"Knapsack Size: {amount} kg\n===============================")

    for i in range(len(itemList)):
        for j in range(amount):
            if i == 0 or j == 0:
                item_grid[i][j] = 0
            elif itemList[i][2] <= j:
                item_grid[i][j] = max(
                    item_grid[i - 1][j],
                    item_grid[i - 1][j - itemList[i][2]] + itemList[i][1],
                )
            else:
                item_grid[i][j] = item_grid[i - 1][j]

    total = item_grid[-1][-1]
    print(f"Total: {total} THB")


def main(item, num):

    knapsack_v2(num, item)


main(json.loads(input()), int(input()))
