def merge_child_into_parent(child, dfs_env):
    parent = child["parent"]
    parent["a"] = parent["a"] + child["a"]
    parent["b"] = parent["b"] + child["b"]

    for grandchild in child["children"].values():
        parent["children"][grandchild["id"]] = grandchild
        grandchild["parent"] = parent

    parent["children"].pop(child["id"])
    dfs_env["dfs"][child["id"]] = False
    child["merged"] = True
