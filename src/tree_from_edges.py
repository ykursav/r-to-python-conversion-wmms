from typing import OrderedDict
import pandas as pd

#' Create a tree of environments from a dataframe of edges
#'
#' Create a tree from a data frame, one row per edge.
#'
#' @details
#' Create a tree from a data frame, one row per edge, with the columns:
#'
#' * `from` ID of a node.
#' * `to` ID of a child of `from`.
#'
#' The edges don't have to be of a directed tree.  The tree will be made
#' directed later by [directed()].
#'
#' For each row, an environment is created that contains the `id` of that row.
#' The environment also contains another environment, `children`, which contains
#' an environment for each child node.  Finally it contains a logical value
#' `merged`, initialised to `FALSE`.
#'
#' One more environment is created to contain all the other environments
#' ("nodes"), named by their `id`.  That environment is what this function
#' returns.
#'
#' @param `edges` A data frame with the columns `from` (ID of a node) and `to`
#'   (ID of a child node of `from`), such as you get from
#'   [emstreeR::ComputeMST()].
#'
#' @return
#' An environment containing one environment (node) per node ID in `edges`,
#' either the `to` or the `from` column.
#'
#' * `id` (`character`).
#' * `original_children`, an environment that is a list of environments, one for
#'   each child of the node.  It is called `original_children` because copies
#'   will later be made that might be pruned.
#' * `merged`, a logical value initialised to `FALSE`.


def tree_from_edges(edges: pd.DataFrame):
    from_ = list(edges["from"].astype(str))
    to = list(edges["to"].astype(str))
    from2 = from_.copy()
    from2.extend(to)
    ids = list(dict.fromkeys(from2))
    tree = {}
    for i in range(0, len(ids)):
        node = {}
        node["id"] = ids[i]
        node["original_children"] = {}
        node["merged"] = False
        tree[ids[i]] = node

    for i in range(0, len(from_)):
        from_id = from_[i]
        to_id = to[i]
        parent = tree[from_id]
        child = tree[to_id]
        # parent
        parent["original_children"][to_id] = child
        # child
        child["original_children"][from_id] = parent

    return tree
