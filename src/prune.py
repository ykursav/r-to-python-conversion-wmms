from src.merge_child_into_parent import merge_child_into_parent


def prune(tree, bounds, dfs_env):
    dfs = dfs_env["dfs"]
    dfs_order = list(dfs.columns)
    dfs_order_copy = dfs_order[1:]
    dfs_order_copy.reverse()
    for node_id in dfs_order_copy:
        node = tree[node_id]

        value = node["a"] / node["b"]
        is_low = value < bounds["low"]
        n_children = len(node["children"])

        while is_low and n_children == 1:
            child = node["children"].values()[0]
            merge_child_into_parent(child, dfs_env)
            value = node["a"] / node["b"]
            is_low = value < bounds["low"]
            n_children = len(node["children"])

        if is_low:
            if n_children == 0:
                node["parent"]["children"].pop(node["id"])
                dfs_env["dfs"][node["id"]] = False
                continue
            continue

        is_high = value >= bounds["high"]
        if is_high:
            merge_child_into_parent(node, dfs_env)
            continue

    node = tree[dfs_order[0]]
    is_low = value < bounds["low"]
    n_children = len(node["children"])

    while is_low and n_children == 1:
        child = node["children"].values()[0]
        merge_child_into_parent(child, dfs_env)
        value = node["a"] / node["b"]
        is_low = value < bounds["low"]
        n_children = len(node["children"].values())
