#!/usr/bin/env python

"""Saves the list of parameters into a text file.

Usage:
$ ./extras/scripts/dayabay-print-parameters-text.py output/parameters.txt
"""

from __future__ import annotations

from argparse import Namespace

from dag_modelling.tools.logger import set_verbosity

from dayabay_model import model_dayabay


def main(opts: Namespace) -> None:
    if opts.verbose:
        set_verbosity(opts.verbose)

    model = model_dayabay(path_data=opts.path_data, parameter_values=opts.par)
    storage = model.storage

    storage["parameters.all"].to_text_file(opts.output)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Print all the parameters to a text file")
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument("output", help="file to print parameters to", metavar="file")
    parser.add_argument(
        "--path-data",
        default=None,
        help="Path to data",
    )

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
