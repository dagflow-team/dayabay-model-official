#!/usr/bin/env python

"""Saves the current values, central values and uncertainties of the parameters to the tex file to
be used with [LaTeX datax](https://ctan.org/pkg/datax) package.

Usage:
$ ./extras/scripts/dayabay-save-parameters-to-latex-datax.py output/dayabay_parameters_datax.tex
"""

from __future__ import annotations

from argparse import Namespace

from dag_modelling.tools.logger import set_verbosity

from dayabay_model_official import model_dayabay


def main(opts: Namespace) -> None:
    if opts.verbose:
        set_verbosity(opts.verbose)

    model = model_dayabay(parameter_values=opts.par)
    storage = model.storage

    storage["parameters.all"].to_datax(opts.output)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Save information on parameters into latex file to be loaded with `datax` package")
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument("output", help="tex file to save parameters", metavar="tex")
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
