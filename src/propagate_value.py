def propagate_value(tree, dfs_order):
    for node_id in dfs_order[1:]:
        node = tree[node_id]
        if node["merged"]:
            parent = node["parent"]
            node["value"] = parent["value"]
            node["ancestor_id"] = parent["ancestor_id"]
            continue

        node["value"] = node["a"] / node["b"]
        node["ancestor_id"] = node["id"]
