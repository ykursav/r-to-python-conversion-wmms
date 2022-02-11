def restore_subtree(tree, dfs_order):
    for node_id in dfs_order:
        node = tree[node_id]
        node["parent"] = node["original_parent"]
        node["a"] = node["original_a"]
        node["b"] = node["original_b"]
        node["merged"] = False
        node["children"] = node["original_children"].copy()
