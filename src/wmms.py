from logging import root
from this import d
from turtle import update
from src.tree_from_edges import tree_from_edges
from src.directed_depth_first import directed_depth_first
from src.set_subtrees import set_subtrees
from src.restore_subtree import restore_subtree
from src.median_value import median_value
from src.value import value
from src.update_bounds import update_bounds
from src.prune import prune
from src.propagate_value import propagate_value
from src.report_tree import report_tree


def weighted_maximum_mean_subtree(tree, dfs_env):
    restore_subtree(tree, dfs_env["dfs"])

    bounds = {"low": float("-inf"), "high": float("inf")}

    while dfs_env["dfs"][dfs_env["dfs"]].dropna(axis=1).shape[1] > 1:
        dfs = dfs_env["dfs"]
        dfs_order = list(dfs[dfs].dropna(axis=1).columns)
        estimate = median_value(tree, bounds, dfs_order)

        greedy_value = value(tree, estimate, dfs_order)

        bounds = update_bounds(bounds, estimate, greedy_value)

        prune(tree, bounds, dfs_env)


def weighted_maximum_mean_subtrees(edges, root_id):
    root_id = str(root_id)
    tree = tree_from_edges(edges)
    d = directed_depth_first(tree, edges, root_id)

    edges = d["edges"]
    dfs_order = d["dfs_order"]
    not_root_id = dfs_order[1:]

    tree = set_subtrees(tree, dfs_order)

    for node in tree[root_id]["original_children"].values():
        node["a"] = node["original_a"]
        node["b"] = node["original_b"]

    tree[root_id]["depth"] = 0

    for node_id in not_root_id:
        node = tree[node_id]
        node["depth"] = node["original_parent"]["depth"] + 1

    for node_id in not_root_id:
        node = tree[node_id]
        if not node["merged"] and node["subtree_dfs"]["dfs"].shape[1] != 1:
            weighted_maximum_mean_subtree(tree=tree, dfs_env=node["subtree_dfs"])

    propagate_value(tree, dfs_order)

    report_tree(edges, tree)

    return edges
