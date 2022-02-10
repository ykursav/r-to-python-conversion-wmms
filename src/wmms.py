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

def weighted_maximum_mean_subtree(tree, dfs_env):
    restore_subtree(tree, dfs_env["dfs"])

    bounds = {"low": float("-inf"), "high": float("inf")}

    while len(dfs_env["dfs"][dfs_env]["dfs"]) > 1:
        dfs = dfs_env["dfs"]
        dfs_order = list(dfs.columns)
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

    for key in tree.keys():
        node = tree[key]
        node["a"] = node["original_a"]
        node["b"] = node["original_b"]

    tree[root_id]["depth"] = 0

    for node_id in not_root_id:
        node = tree[node_id]
        node["depth"] = node["original_parent"]["depth"] + 1

    for node_id in not_root_id:
        node = tree[node_id]
        if(not node["merged"] and len(node["subtree_dfs"]["dfs"]) != 1):
            weighted_maximum_mean_subtree(tree=tree, dfs_env=node["subtree_dfs"])


    propagate_value(tree, dfs_order)



weighted_maximum_mean_subtrees <- function(edges, root_id) {

  # Propagate node values down from the children of the root.
  propagate_value(tree, dfs_order)
  # Return the original edgelist, now directed and with `ancestor` and `value`
  # columns to describe the tree's final state.
  report_tree(d$edges, tree)
}

#' Maximise one subtree
#'
#' After preparing the tree by making it directed and finding a depth-first
#' search order, [weighted_maximum_mean_subtrees()] applies this function
#' recursively to nodes that haven't yet been merged into an optimum subtree.
#'
#' @param `dfs_env` (`environment`) An environment containing an object called
#'   `dfs` that is a named list of `NULL` values, where the names are IDs of
#'   nodes in depth-first order.  Obtained from [set_subtrees()].
#' @param `tree` (`environment`) The whole tree, originally created by
#'   [tree_from_edges()].
#'
#' @return
#' There is no return value.  The `tree` is modified in place.

weighted_maximum_mean_subtree <- function(tree, dfs_env) {
  # (re)set the nodes in the subtree to their original state.
  restore_subtree(tree, names(dfs_env$dfs))
  # The algorithm searches for the true value between two bounds.  Begin with
  # bounds infinitely wide.
  bounds <- list(low = -Inf, high = Inf)
  # Then loop until the maximum is achieved, which will be when the root has
  # zero children.
  while (length(dfs_env$dfs[dfs_env$dfs]) > 1L) { # At 1, only the subtree's root is left.
    dfs <- dfs_env$dfs
    dfs_order <- names(dfs[dfs])
    # Estimate the true maximum of sum(a)/sum(b) of a rooted subtree as the
    # median of the a/b values of each node, discarding any a/b that is
    # outside the bounds.
    estimate <- median_value(tree, bounds, dfs_order)
    # Calculate the value of subtree obtained by greedily pruning to achieve
    # the estimate.
    greedy_value <- value(tree, estimate, dfs_order)
    # The greedy value rules out part of the search space, depending on which
    # side of the estimate it is.  So update the bounds.
    bounds <- update_bounds(bounds, estimate, greedy_value)
    # It's now safe to prune leaf nodes whose a/b is below the bounds, and to
    # combine other nodes whose a/b is above the bounds with their parent.
    prune(tree, bounds, dfs_env)
  }
  NULL
  )

