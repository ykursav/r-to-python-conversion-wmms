from typing import List
from statistics import median


def median_value(tree, bounds, dfs_order: List):
    values = []
    i = 0
    dfs_order_copy = dfs_order.copy()
    dfs_order_copy.reverse()
    for node_id in dfs_order_copy:
        node = tree[node_id]
        value = node["a"] / node["b"]
        if value >= bounds["low"] and value <= bounds["high"]:
            values.append(value)
            i += 1

    return median(values)
