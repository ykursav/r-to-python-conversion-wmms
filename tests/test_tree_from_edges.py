from src.tree_from_edges import tree_from_edges
import pandas as pd
from src.directed_depth_first import directed_depth_first
from src.set_subtrees import set_subtrees

from_ = list(range(2, 8)) * 5
to = list(range(2, 33))
a = list(range(1, 6)) * 6
a.insert(0, 10)
b = 1
from_.sort()
from_.insert(0, 1)
data = {"from": from_, "to": to, "a": a, "b": b}


def test_tree_from_edges():
    df = pd.DataFrame(data)
    tree = tree_from_edges(df)

    root_id = "1"
    tree[root_id]["original_parent"] = {"id": ["0"]}
    stack = []
    stack.append(tree[root_id])
    n = df.shape[0] + 1
    dfs_order = [""] * n
    parents = [""] * n
    i = 0
    x = directed_depth_first(tree, df, "1")


def test_directed_depth_first():
    pass


def test_sub_trees():
    df = pd.DataFrame(data)
    tree = tree_from_edges(df)

    root_id = "1"
    tree[root_id]["original_parent"] = {"id": ["0"]}
    stack = []
    stack.append(tree[root_id])
    n = df.shape[0] + 1
    dfs_order = [""] * n
    parents = [""] * n
    i = 0
    x = directed_depth_first(tree, df, "1")
    set_subtrees(tree, x["dfs_order"])
