from src.ComputeMST import compute_mst
import numpy as np
import pandas as pd
from src.tree_from_edges import tree_from_edges

if __name__ == "__main__":
    np.random.seed(1984)
    n = 15
    c1 = pd.DataFrame(
        {"x": np.random.normal(-0.2, 0.2, n), "y": np.random.normal(-2, 0.2, n)}
    )
    c2 = pd.DataFrame(
        {"x": np.random.normal(-1.1, 0.15, n), "y": np.random.normal(-2, 0.3, n)}
    )
    d = c1.append(c2, ignore_index=True)
    computed_df = compute_mst(d)
    tree = tree_from_edges(computed_df)
    print(tree)
    print(len(tree["25"]))
    # computed_df.to_csv("output.csv")
