#!/usr/bin/env python

"""Prints the selected paths from the internal storage.

Examples:
- Print free parameters
$ ./extras/scripts/dayabay-print-internal-data.py --print parameters.free
"""

from __future__ import annotations

from argparse import Namespace

from dag_modelling.tools.logger import set_verbosity
from matplotlib import pyplot as plt
from numpy import ma

from dayabay_model_official import model_dayabay

plt.rcParams.update(
    {
        "axes.formatter.use_mathtext": True,
        "axes.grid": False,
        "xtick.minor.visible": True,
        "xtick.top": True,
        "ytick.minor.visible": True,
        "ytick.right": True,
        "axes.formatter.limits": (-3, 4),
        "figure.max_open_warning": 30,
    }
)


def main(opts: Namespace) -> None:
    if opts.verbose:
        set_verbosity(opts.verbose)

    model = model_dayabay(parameter_values=opts.par)

    storage = model.storage

    matrix_iav = storage["outputs.detector.iav.matrix_rescaled.AD11"].data.copy()
    matrix_lsnl = storage["outputs.detector.lsnl.matrix.AD11"].data.copy()
    matrix_eres = storage["outputs.detector.eres.matrix"].data.copy()
    matrix_total = matrix_eres @ (matrix_lsnl @ matrix_iav)

    matshow_kwargs = {"extent": (0, 12, 12, 0)}
    plt.figure()
    ax = plt.subplot(
        111,
        xlabel="Deposited energy, MeV",
        ylabel="Energy, deposited in scintillator, MeV",
        title="Daya Bay IAV matrix (log scale)",
    )
    mappable = ax.matshow(
        ma.array(matrix_iav, mask=(matrix_iav == 0.0)),
        norm="log",
        **matshow_kwargs,
    )
    plt.colorbar(mappable)

    plt.figure()
    ax = plt.subplot(
        111,
        xlabel="Energy, deposited in scintillator, MeV",
        ylabel="Visible energy, MeV",
        title="Daya Bay LSNL matrix",
    )
    mappable = ax.matshow(ma.array(matrix_lsnl, mask=(matrix_lsnl == 0.0)), **matshow_kwargs)
    plt.colorbar(mappable)

    plt.figure()
    ax = plt.subplot(
        111,
        xlabel="Visible energy, MeV",
        ylabel="Reconstructed energy, MeV",
        title="Daya Bay Energy resolution matrix",
    )
    mappable = ax.matshow(ma.array(matrix_eres, mask=(matrix_eres == 0.0)), **matshow_kwargs)
    plt.colorbar(mappable)

    plt.figure()
    ax = plt.subplot(
        111,
        xlabel="Deposited energy, MeV",
        ylabel="Reconstructed energy, MeV",
        title="Daya Bay detector energy response matrix",
    )
    mappable = ax.matshow(ma.array(matrix_total, mask=(matrix_total == 0.0)), **matshow_kwargs)
    plt.colorbar(mappable)

    plt.show()


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
