from src.ComputeMST import compute_mst
import pandas as pd
from pandas.testing import assert_frame_equal
from src.tree_from_edges import tree_from_edges
from src.directed_depth_first import directed_depth_first

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

expected = {
    "from": [
        11,
        8,
        3,
        5,
        6,
        8,
        1,
        10,
        1,
        8,
        2,
        9,
        4,
        1,
    ],
    "to": [
        13,
        12,
        7,
        6,
        7,
        10,
        2,
        14,
        5,
        13,
        4,
        12,
        9,
        1,
    ],
    "distance": [
        0.03281747,
        0.05703382,
        0.08060398,
        0.11944501,
        0.13450475,
        0.14293342,
        0.15875908,
        0.16993335,
        0.24918237,
        0.27882008,
        0.34485145,
        0.36016689,
        0.37023475,
        0.00000000,
    ],
}

df_input = pd.DataFrame(input)
df_expected = pd.DataFrame(expected)
df_full_expected = pd.concat([df_input, df_expected], axis=1)

df_result = compute_mst(df_input)

tree = tree_from_edges(df_result)


def test_directed_depth_first():
    root_id = "1"
    edges = df_result
    d = directed_depth_first(tree, edges, root_id)


def test_tree_from_edges():
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

    expected = {
        "from": [
            11,
            8,
            3,
            5,
            6,
            8,
            1,
            10,
            1,
            8,
            2,
            9,
            4,
            1,
        ],
        "to": [
            13,
            12,
            7,
            6,
            7,
            10,
            2,
            14,
            5,
            13,
            4,
            12,
            9,
            1,
        ],
        "distance": [
            0.03281747,
            0.05703382,
            0.08060398,
            0.11944501,
            0.13450475,
            0.14293342,
            0.15875908,
            0.16993335,
            0.24918237,
            0.27882008,
            0.34485145,
            0.36016689,
            0.37023475,
            0.00000000,
        ],
    }

    df_input = pd.DataFrame(input)
    df_expected = pd.DataFrame(expected)
    df_full_expected = pd.concat([df_input, df_expected], axis=1)

    df_result = compute_mst(df_input)

    tree = tree_from_edges(df_result)

    print("End")


def test_compute_mst():
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

    expected = {
        "from": [
            11,
            8,
            3,
            5,
            6,
            8,
            1,
            10,
            1,
            8,
            2,
            9,
            4,
            1,
        ],
        "to": [
            13,
            12,
            7,
            6,
            7,
            10,
            2,
            14,
            5,
            13,
            4,
            12,
            9,
            1,
        ],
        "distance": [
            0.03281747,
            0.05703382,
            0.08060398,
            0.11944501,
            0.13450475,
            0.14293342,
            0.15875908,
            0.16993335,
            0.24918237,
            0.27882008,
            0.34485145,
            0.36016689,
            0.37023475,
            0.00000000,
        ],
    }

    df_input = pd.DataFrame(input)
    df_expected = pd.DataFrame(expected)
    df_full_expected = pd.concat([df_input, df_expected], axis=1)

    # when
    df_result = compute_mst(df_input)

    assert_frame_equal(df_full_expected, df_result)
