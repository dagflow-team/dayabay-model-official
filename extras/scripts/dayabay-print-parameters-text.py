#!/usr/bin/env python

"""Saves the list of parameters into a text file.

Usage:
$ ./extras/scripts/dayabay-print-parameters-text.py output/parameters.txt
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
    storage = model.storage

    storage["parameters.all"].to_text_file(opts.output)


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

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument("output", help="file to print parameters to", metavar="file")
    parser.add_argument(
        "-s",
        "--source-type",
        "--source",
        choices=("tsv", "hdf5", "root", "npz"),
        default="default:hdf5",
        help="Data source type",
    )

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
