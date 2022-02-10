from numpy import empty
import pandas as pd

# not complete check again
def set_subtrees(tree, dfs_order):
    for node in tree.values():
        subtree_dfs = {}
        subtree_dfs["dfs"] = None
        node["subtree_dfs"] = subtree_dfs

    for node_id in dfs_order:
        node = tree[str(node_id)]
        subtree_dfs = node["subtree_dfs"]
        self = pd.DataFrame({node_id: [True]})
        if subtree_dfs:
            subtree_dfs["dfs"] = pd.concat([self, subtree_dfs["dfs"]], axis=1)
        else:
            subtree_dfs["dfs"] = self

        if "subtree_dfs" in node["original_parent"]:
            parent_subtree_dfs = node["original_parent"]["subtree_dfs"]
            parent_subtree_dfs["dfs"] = pd.concat(
                [subtree_dfs["dfs"], parent_subtree_dfs["dfs"]], axis=1
            )

    return tree
