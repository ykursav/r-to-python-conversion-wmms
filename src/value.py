def value(tree, cutoff, dfs_order):
    for node_id in dfs_order:
        node = tree[node_id]
        node["sub_a"] = node["a"]
        node["sub_b"] = node["b"]
    dfs_order_copy = dfs_order[1:].copy()
    dfs_order_copy.reverse()
    for node_id in dfs_order_copy:
        node = tree[node_id]
        value = node["sub_a"] / node["sub_b"]

        if value < cutoff:
            continue
        else:
            parent = node["parent"]
            parent["sub_a"] = parent["sub_a"] + node["sub_a"]
            parent["sub_b"] = parent["sub_b"] + node["sub_b"]

    subroot = tree[dfs_order[0]]
    return subroot["sub_a"] / subroot["sub_b"]
