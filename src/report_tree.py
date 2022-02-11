def report_tree(edges, tree):
    n = edges.shape[0]
    depth = [0] * n
    ancestor = [""] * n
    value = [0.0] * n
    i = 0
    for node_id in edges["to"]:
        node_id = str(node_id)
        node = tree[str(node_id)]
        depth[i] = int(node["depth"])
        ancestor[i] = str(node["ancestor_id"])
        value[i] = float(node["value"])
        i = i + 1

    edges["depth"] = depth
    edges["ancestor"] = ancestor
    edges["value"] = value

    return edges
