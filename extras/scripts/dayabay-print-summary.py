#!/usr/bin/env python

"""Prints Daya Bay summary data to stdout.

Yields 4 tables: for each of 3 data taking periods and a total one. The results correspond to the
Table I from Physical Review Letters 130, 161802 (2023). The output is transposed so the column when
viewed may be set to a specific data type, e.g. in `visidata`.

Supported formats: tsv/txt (including archived .gz and .bz2), hdf5, npz, and root.

Usage:
- Print the summary to txt file:
$ ./extras/scripts/dayabay-print-summary.py output/dayabay_summary.txt
- Print the summary to npz file and stdout:
$ ./extras/scripts/dayabay-print-summary.py output/dayabay_summary.npz -
"""

from __future__ import annotations

from argparse import Namespace
from typing import TYPE_CHECKING

from dag_modelling.tools.logger import set_verbosity
from dag_modelling.tools.save_records import save_records

from dayabay_model_official import model_dayabay

if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Any


def main(opts: Namespace) -> None:
    if opts.verbose:
        set_verbosity(opts.verbose)

    model = model_dayabay(parameter_values=opts.par)

    save_summary(model, opts.output)


def save_summary(model: Any, filenames: Sequence[str]):
    data = {}
    try:
        for period in ["total", "6AD", "8AD", "7AD"]:
            data[period] = model.make_summary_table(period=period)
    except AttributeError:
        return

    save_records(data, filenames, tsv_allow_no_key=True, to_records_kwargs={"index": False})


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Print Daya Bay summary")
    parser.add_argument(
        "output",
        nargs="+",
        help="location to print summary data to",
    )
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument(
        "-s",
        "--source-type",
        "--source",
        choices=("tsv", "hdf5", "root", "npz"),
        default="default:hdf5",
        help="Data source type",
    )

    plot = parser.add_argument_group("plot", "plotting related options")
    plot.add_argument("--plots-all", help="plot all the nodes to the folder", metavar="folder")
    plot.add_argument(
        "--plots",
        nargs="+",
        help="plot the nodes in storages",
        metavar=("folder", "storage"),
    )

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
