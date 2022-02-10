def value(tree, cutoff, dfs_order):
    for node_id in dfs_order:
        node = tree[node_id]
        node["sub_a"] = node["a"]
        node["sub_b"] = node["b"]
    dfs_order_copy = dfs_order[1:].copy()
    dfs_order_copy.reverse()
    for node_id in dfs_order_copy:
        node = tree["node_id"]
        value = node["sub_a"] / node["sub_b"]

        if (value < cutoff):
            continue
        else:
            parent = node["parent"]
            parent["sub_a"] = parent["sub_a"] + node["sub_a"]
            parent["sub_b"] = parent["sub_b"] + node["sub_b"]

    subroot = tree[dfs_order[0]]
    return subroot["sub_a"] / subroot["sub_b"]



value <- function(tree, cutoff, dfs_order) {
  # Traverse the nodes twice.
  # First time: initialise the subtotals `sub_a` and `sub_b` to the actual `a`
  # and `b` of each node.  The subtotals will be incremented instead of `a` and
  # `b` themselves, because this is a temporary calculation.
  for (node_id in dfs_order) {
    node <- tree[[node_id]]
    node$sub_a <- node$a
    node$sub_b <- node$b
  }
  # Second time: leaves first, calculate and propagate values.
  # [-1] omits the root node of this subtree, because it can't propagate its
  # value to its parent.
  for (node_id in rev(dfs_order[-1])) {
    node <- tree[[node_id]]
    # Calculate the temporary value
    value <- node$sub_a / node$sub_b
    # Skip if the value is below the cutoff
    if (value < cutoff) next
    # Otherwise add a and b to the parent
    parent <- node$parent
    parent$sub_a <- parent$sub_a + node$sub_a
    parent$sub_b <- parent$sub_b + node$sub_b
  }
  # Return the value of the root of this subtree
  subroot <- tree[[dfs_order[1]]]
  subroot$sub_a / subroot$sub_b
}