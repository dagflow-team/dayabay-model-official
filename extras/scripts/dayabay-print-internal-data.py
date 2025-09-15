#!/usr/bin/env python

"""Prints the selected paths from the internal storage.

Examples:
- Print free parameters
$ ./extras/scripts/dayabay-print-internal-data.py --print parameters.free
- Print constrained parameters
$ ./extras/scripts/dayabay-print-internal-data.py --print parameters.constrained
- Print free and constrained parameters
$ ./extras/scripts/dayabay-print-internal-data.py --print parameters.free parameters.constrained
- Print constants
$ ./extras/scripts/dayabay-print-internal-data.py --print parameters.constant
- Print outputs (array)
$ ./extras/scripts/dayabay-print-internal-data.py --print outputs
"""

from __future__ import annotations

from argparse import Namespace

from dag_modelling.tools.logger import set_verbosity

from dayabay_model_official import model_dayabay


def main(opts: Namespace) -> None:
    if opts.verbose:
        set_verbosity(opts.verbose)

    model = model_dayabay(source_type=opts.source_type, parameter_values=opts.par)

    storage = model.storage

    default_mode = not opts.print_all and not opts.print
    if default_mode:
        opts.print = ["outputs"]
    if opts.print_all:
        print(storage.to_table(truncate="auto", df_kwargs={"columns": opts.print_columns}))
    for sources in opts.print:
        for source in sources:
            print(
                storage(source).to_table(
                    truncate="auto",
                    df_kwargs={
                        "columns": opts.print_columns,
                        "parent_key": source,
                    },
                )
            )


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument(
        "--source-type",
        choices=("tsv", "hdf5", "root", "npz"),
        default="default:hdf5",
        help="Data source type",
    )

    storage = parser.add_argument_group("storage", "storage related options")
    storage.add_argument("-P", "--print-all", action="store_true", help="print all")
    storage.add_argument("-p", "--print", action="append", nargs="+", default=[], help="print all")
    storage.add_argument("--print-columns", "--pc", default=None, nargs="+", help="Print columns")

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
