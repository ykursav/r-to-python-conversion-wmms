from src.ComputeMST import compute_mst
import pandas as pd
from src.wmms import weighted_maximum_mean_subtrees
import numpy as np

# Input data
input = {
    "x": [
        -0.118159357,
        -0.264604994,
        -0.072829535,
        -0.569225757,
        -0.009270527,
        0.037697969,
        -0.091509110,
        -1.097338236,
        -0.841400898,
        -1.081888729,
        -1.366334073,
        -1.081078171,
        -1.357063682,
        -0.913706515,
    ],
    "y": [
        2.166545,
        2.105242,
        1.716803,
        1.943598,
        1.942413,
        1.832590,
        1.795213,
        1.871078,
        2.194585,
        1.728982,
        2.003965,
        1.925745,
        1.972485,
        1.753315,
    ],
}

np.random.seed(1984)
n = 7
c1 = pd.DataFrame(
    {"x": np.random.normal(-0.2, 0.2, n), "y": np.random.normal(-2, 0.2, n)}
)
c2 = pd.DataFrame(
    {"x": np.random.normal(-1.1, 0.15, n), "y": np.random.normal(-2, 0.3, n)}
)
d = c1.append(c2, ignore_index=True)

# Set dataframe ( if you feed some predetermined data )
# df = pd.DataFrame(input)

# mst_results
# mst_result = compute_mst(df)


# mst_results
mst_result = compute_mst(d)


mst_result = mst_result.sort_values(by="from")
# set a and b
mst_result["a"] = [10, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
mst_result["b"] = 1

# wmms
from_ = list(range(2, 8)) * 5
to = list(range(2, 33))
a = list(range(1, 6)) * 6
a.insert(0, 10)
b = 1
from_.sort()
from_.insert(0, 1)
data = {"from": from_, "to": to, "a": a, "b": b}
root_id = "1"
data_input_wmms = pd.DataFrame(data)
data_input_wmms["a"] = -data_input_wmms["a"]
maximum = weighted_maximum_mean_subtrees(data_input_wmms, root_id)

maximum["a"] = -maximum["a"]
maximum["value"] = -maximum["value"]

print(maximum)
print("Completed")
