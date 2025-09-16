#!/usr/bin/env python

"""Saves the detector response matrices and, optionally, plots them.

Example. Save matrices to 4 different output types and also plot and show images and save them as pdf:
$ ./extras/scripts/dayabay-save-detector-response-matrices.py --output output/matrix.tsv \
                                                                       output/matrix.npz \
                                                                       output/matrix.root \
                                                                       output/matrix.hdf5 \
                                                               --plot-output output/matrix{}.pdf \
                                                               --show

While npz/hdf5/root support having multiple matrices in a single file, for tsv multiple matrices are
saved as distinct file `key.tsv` in the `output/matrix.tsv` folder.
"""

from __future__ import annotations

from argparse import Namespace

from dag_modelling.tools.logger import set_verbosity
from dag_modelling.tools.save_matrices import save_matrices
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

    model = model_dayabay(source_type=opts.source_type, parameter_values=opts.par)

    storage = model.storage

    matrix_iav = storage["outputs.detector.iav.matrix_rescaled.AD11"].data.copy()
    matrix_lsnl = storage["outputs.detector.lsnl.matrix.AD11"].data.copy()
    matrix_eres = storage["outputs.detector.eres.matrix"].data.copy()
    matrix_total = matrix_eres @ (matrix_lsnl @ matrix_iav)

    output_data = {
        "matrix_iav": matrix_iav,
        "matrix_lsnl": matrix_lsnl,
        "matrix_eres": matrix_eres,
        "matrix_total": matrix_total,
    }
    save_matrices(output_data, opts.output)

    if not (opts.show or opts.plot_output):
        return

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
    cbar = plt.colorbar(mappable)
    cbar.solids.set_rasterized(True)  # pyright: ignore [reportOptionalMemberAccess]
    if opts.plot_output:
        filename = opts.plot_output.format("_iav")
        plt.savefig(filename)
        print(f"Write: {filename}")

    plt.figure()
    ax = plt.subplot(
        111,
        xlabel="Energy, deposited in scintillator, MeV",
        ylabel="Visible energy, MeV",
        title="Daya Bay LSNL matrix",
    )
    mappable = ax.matshow(ma.array(matrix_lsnl, mask=(matrix_lsnl == 0.0)), **matshow_kwargs)
    cbar = plt.colorbar(mappable)
    cbar.solids.set_rasterized(True)  # pyright: ignore [reportOptionalMemberAccess]
    if opts.plot_output:
        filename = opts.plot_output.format("_lsnl")
        plt.savefig(filename)
        print(f"Write: {filename}")

    plt.figure()
    ax = plt.subplot(
        111,
        xlabel="Visible energy, MeV",
        ylabel="Reconstructed energy, MeV",
        title="Daya Bay Energy resolution matrix",
    )
    mappable = ax.matshow(ma.array(matrix_eres, mask=(matrix_eres == 0.0)), **matshow_kwargs)
    cbar = plt.colorbar(mappable)
    cbar.solids.set_rasterized(True)  # pyright: ignore [reportOptionalMemberAccess]
    if opts.plot_output:
        filename = opts.plot_output.format("_eres")
        plt.savefig(filename)
        print(f"Write: {filename}")

    plt.figure()
    ax = plt.subplot(
        111,
        xlabel="Deposited energy, MeV",
        ylabel="Reconstructed energy, MeV",
        title="Daya Bay detector energy response matrix",
    )
    mappable = ax.matshow(ma.array(matrix_total, mask=(matrix_total == 0.0)), **matshow_kwargs)
    cbar = plt.colorbar(mappable)
    cbar.solids.set_rasterized(True)  # pyright: ignore [reportOptionalMemberAccess]
    if opts.plot_output:
        filename = opts.plot_output.format("_total")
        plt.savefig(filename)
        print(f"Write: {filename}")

    if opts.show:
        plt.show()


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Save detector response matrices")
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument(
        "--source-type",
        choices=("tsv", "hdf5", "root", "npz"),
        default="default:hdf5",
        help="Data source type",
    )

    parser.add_argument("-s", "--show", action="store_true", help="show the figures")

    output = parser.add_argument_group("output", "control the ouputs")
    output.add_argument("-o", "--output", nargs="+", required=True, help="output files to save")
    output.add_argument("--plot-output", help="output file to save plots ({} to specify type)")

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
