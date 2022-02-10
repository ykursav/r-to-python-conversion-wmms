from re import U
from typing import Dict
import pandas as pd
import numpy as np

#' Make an EMST directed and return the depth-first search order
#'
#' Euclidean Minimum Spanning Tree (EMST) edgelists from
#' [emstreeR::ComputeMST()] aren't directed.  We also need to know a depth-first
#' search order of the nodes, to traverse them in loops rather than by
#' recursion, which would reach the stack limit.  This function does both.  A
#' list is returned containing the modified `edges`, and a `dfs_order` element
#' that names the nodes in depth-first search order.  The `tree` is modified in
#' place.
#'
#' @param `tree` (`environment`) A potentially undirected tree, originally from
#'   [tree_from_edges()].
#' @param `edges` A data frame with one row per edge, and at least the two
#'   `numeric` columns `from` and `to` for the IDs of the nodes being connected
#'   by the edge.  Must be the same as was used by [tree_from_edges()] to create
#'   `tree` from the output of [emstreeR::ComputeMST()].
#' @param `root_id` (`numeric`) The ID of the node to treat as the root.
#'
#' @return
#' A list containing `edges` with some values of the `to` and `from` columns
#' exchanged so that the graph is directed, and `dfs_order`, which is a vector
#' of node IDs in the order that they would be visited in a depth-first search.
#' the `tree` is modified in place, so is not returned.


def directed_depth_first(tree, edges: pd.DataFrame, root_id) -> Dict:
    tree[root_id]["original_parent"] = {"id": "0"}
    stack = []
    stack.append(tree[root_id])
    n = edges.shape[0] + 1
    dfs_order = [""] * n
    parents = [""] * n
    i = 0
    while len(stack) > 0:

        node = stack[0]
        stack.pop(0)

        dfs_order[i] = node["id"]
        parents[i] = node["original_parent"]["id"]

        original_children = list(node["original_children"].values())
        original_children.reverse()

        # original_children_new = original_children.copy()
        for child in original_children:
            child["original_children"].pop(node["id"])
            child["original_parent"] = node

        stack = original_children + stack

        i += 1

    # parents_dict = {}
    # for i in range(0, len(parents)):
    #     parents_dict[i] = parents[i]

    parents_series = pd.Series(
        data=[float(elem) for elem in parents],
        index=[float(elem) for elem in dfs_order],
    )

    orig_from = edges["from"]
    exchange_which = np.where(
        edges["from"].values != parents_series.reindex(edges["to"].values)
    )[0]
    for exchange in exchange_which:
        edges["from"][exchange] = edges["to"][exchange]
        edges["to"][exchange] = orig_from[exchange]

    edges_to = edges["to"].astype(str)
    a = edges["a"]
    b = edges["b"]
    for j in range(0, (n - 1)):
        node = tree[edges_to[j]]
        node["original_a"] = a[j]
        node["original_b"] = b[j]

    return {"edges": edges, "dfs_order": dfs_order}
