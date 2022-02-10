from typing import List
from statistics import median


def median_value(tree, bounds, dfs_order: List):
    values = []
    i = 0
    dfs_order.reverse()
    for node_id in dfs_order:
        node = tree[node_id]
        value = node["a"] / node["b"]
        if value >= bounds["low"] and value <= bounds["high"]:
            values.append(value)
            i += 1

    return median(values)
