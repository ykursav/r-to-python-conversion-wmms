from numpy import empty
import pandas as pd

# not complete check again
def set_subtrees(tree, dfs_order):
    for node in tree.values():
        subtree_dfs = {}
        subtree_dfs["dfs"] = pd.DataFrame()
        node["subtree_dfs"] = subtree_dfs

    dfs_order_copy = dfs_order.copy()
    dfs_order_copy.reverse()
    for node_id in dfs_order_copy:
        node = tree[str(node_id)]
        subtree_dfs = node["subtree_dfs"]
        self = pd.DataFrame({node_id: [True]})
        if not subtree_dfs["dfs"].empty:
            subtree_dfs["dfs"] = pd.concat([self, subtree_dfs["dfs"]], axis=1)
        else:
            subtree_dfs["dfs"] = self

        if "subtree_dfs" in node["original_parent"]:
            parent_subtree_dfs = node["original_parent"]["subtree_dfs"]
            if not parent_subtree_dfs["dfs"].empty:
                parent_subtree_dfs["dfs"] = pd.concat(
                    [subtree_dfs["dfs"], parent_subtree_dfs["dfs"]], axis=1
                )
            else:
                parent_subtree_dfs["dfs"] = subtree_dfs["dfs"]
    return tree
