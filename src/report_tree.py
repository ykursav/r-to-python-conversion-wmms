def report_tree(edges, tree):
    n = edges.shape[0]
    depth = 
report_tree <- function(edges, tree) {
  n <- nrow(edges)
  depth    <- .Internal(vector("integer", n))
  ancestor <- .Internal(vector("character", n))
  value    <- .Internal(vector("double", n))
  i <- 0L
  for (node_id in as.character(edges$to)) {
    i <- i + 1L
    node <- tree[[node_id]]
    depth[i] <- node$depth
    ancestor[i] <- node$ancestor_id
    value[i] <- node$value
  }
  edges$depth <- depth
  edges$ancestor <- as.double(ancestor)
  edges$value <- value
  edges
}