import pandas as pd

from mlpack import emst
from src.data_check import data_check
from sklearn.preprocessing import scale
from typing import Dict, List
import numpy as np

#' @title Euclidean Minimum Spanning Tree
#'
#' @description Computes an Euclidean Minimum Spanning Tree (EMST) from the
#'     data. \code{ComputeMST} is a wrapper around the homonym function in
#'     the 'mlpack' library.
#'
#' @param x a \code{numeric matrix} or \code{data.frame}.
#' @param verbose If \code{TRUE}, mutes the output from the C++
#'     code.
#' @param scale If \code{TRUE}, it will scale your data with
#'     \code{\link[base]{scale}} before computing the the minimum spanning tree
#'     and the distances to be presented will refer to the scaled data.
#'
#' @details Before the computation, ComputeMST runs some checks and
#'     transformations (if needed) on the provided data using the
#'     \code{data_check} function. After the computation, it returns the
#'     'cleaned' data plus 3 columns: \code{from}, \code{to}, and
#'     \code{distance}. Those columns show each pair of start and end points,
#'     and the distance between them, forming the Minimum Spanning Tree (MST).
#'
#' @return an object of class \code{MST} and \code{data.frame}.
#'
#' @note It is worth noting that the afore mentioned  columns (\code{from},
#'     \code{to}, and \code{distance}) have no relationship with their
#'     respective row in the output \code{MST/data.frame} object. The authors
#'     chose the \code{data.frame} format for the output rather than a
#'     \code{list} because it is more suitable for plotting the MST with the
#'     new 'ggplot2' Stat (\code{\link[emstreeR]{stat_MST}}) provided with this
#'     package. The last row of the output at these three columns will always
#'     be the same: \code{1 1 0.0000000}. This is because we always have n-1
#'     edges for n points. Hence, this is done to 'complete' the data.frame
#'     that is returned.
#'
#' @examples
#'
#' ## artifical data
#' np.random.seed(1984)
# n = 15
# c1 = pd.DataFrame({"x" : np.random.normal(-0.2, 0.2, n), "y" : np.random.normal(-2, 0.2, n)})
#' c2 = pd.DataFrame({"x" : np.random.normal(-1.1, 0.15, n), "y" : np.random.normal(-2, 0.3, n)})
#' d = c1.append(c2, ignore_index=True)
#'
#' ## MST:
#' out = ComputeMST(d)
#' out
#'
#' @export
#'


def compute_mst(x: pd.DataFrame, verbose=True, scale=False) -> pd.DataFrame:

    data_aux = data_check(x)
    if not scale:
        if not verbose:
            from_to_matrix = pd.DataFrame(emst(data_aux)["output"])
        else:
            from_to_matrix = pd.DataFrame(emst(data_aux)["output"])
            print(from_to_matrix)

        from_ = list(from_to_matrix.iloc[0].astype(int).values)
        from_.append(1)
        to_ = list(from_to_matrix.iloc[1].astype(int).values)
        to_.append(1)
        distance = list(from_to_matrix.iloc[2].values)
        distance.append(0)

    else:
        data_aux = pd.DataFrame(
            scale(data_aux), index=data_aux.index, columns=data_aux.columns
        )

        if not verbose:
            from_to_matrix = pd.DataFrame(emst(data_aux)["output"])
        else:
            from_to_matrix = pd.DataFrame(emst(data_aux)["output"])
            print(from_to_matrix)

        from_ = list(from_to_matrix.iloc[0].astype(int).values)
        from_.append(1)
        to_ = list(from_to_matrix.iloc[1].astype(int).values)
        to_.append(1)
        distance = list(from_to_matrix.iloc[2].values)
        distance.append(0)

    x = extend_dict_on_df(data_aux, {"from": from_})
    x = extend_dict_on_df(x, {"to": to_})
    x = extend_list_as_columns(x, distance)

    return x


def extend_dict_on_df(
    df: pd.DataFrame,
    dict_to_extend: Dict[str, List],
):
    df_copy = df.copy()
    counter = 0
    y_axis = df_copy.shape[0]
    for key, value in dict_to_extend.items():
        print(key)
        print(value)
        df_copy[key] = 0
        while counter < y_axis:
            df_copy.loc[counter, key] = value[counter % len(value)]
            counter += 1

    return df_copy


def extend_list_as_columns(
    df: pd.DataFrame,
    list_to_extend: List,
):
    df_copy = df.copy()
    col_counter = 0
    for elem in list_to_extend:
        col_name = f"col_{str(col_counter)}"
        df_copy[col_name] = elem
        col_counter += 1

    return df_copy


