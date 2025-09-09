#!/usr/bin/env python

"""Plots the contents of all the nodes from `outputs` storage.

Usage:
- Plot all the nodes
$ ./extras/scripts/dayabay-plot-all-nodes.py --plot-all output/model_plots
- Plot all the nodes from `background`
$ ./extras/scripts/dayabay-plot-all-nodes.py --plot output/background_plots background
"""

from __future__ import annotations

from argparse import Namespace

from dag_modelling.tools.logger import set_verbosity
from matplotlib import pyplot as plt

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

    plot_overlay_priority = [
        model.index["isotope"],
        model.index["reactor"],
        model.index["background"],
        model.index["detector"],
        model.index["lsnl"],
    ]
    plot_kwargs = {
        "overlay_priority": plot_overlay_priority,
        "latex_substitutions": latex_substitutions,
        "exact_substitutions": exact_substitutions,
        "savefig_kwargs": {
            "metadata": {"CreationDate": None},
        },
    }
    if opts.plot_all:
        storage("outputs").plot(folder=opts.plot_all, minimal_data_size=10, **plot_kwargs)

    if opts.plot:
        folder, *sources = opts.plot
        for source in sources:
            storage["outputs"](source).plot(
                folder=f"{folder}/{source.replace('.', '/')}",
                minimal_data_size=10,
                **plot_kwargs,
            )


latex_substitutions = {
    " U235": r" $^{235}$U",
    " U238": r" $^{238}$U",
    " Pu239": r" $^{239}$Pu",
    " Pu241": r" $^{241}$Pu",
    "U235 ": r"$^{235}$U ",
    "U238 ": r"$^{238}$U ",
    "Pu239 ": r"$^{239}$Pu ",
    "Pu241 ": r"$^{241}$Pu ",
    "²³⁵U": r"$^{235}$U",
    "²³⁸U": r"$^{238}$U",
    "²³⁹Pu": r"$^{239}$Pu",
    "²⁴¹Pu": r"$^{241}$Pu",
    "Eν": r"$E_{\nu}$",
    "Edep": r"$E_{\rm dep}$",
    "Evis": r"$E_{\rm vis}$",
    "Escint": r"$E_{\rm scint}$",
    "Erec": r"$E_{\rm rec}$",
    "cosθ": r"$\cos\theta$",
    "Δm²₃₁": r"$\Delta m^2_{31}$",
    "Δm²₃₂": r"$\Delta m^2_{32}$",
    "Δm²₂₁": r"$\Delta m^2_{21}$",
    "sin²2θ₁₃": r"$\sin^22\theta_{13}$",
    "sin²2θ₁₂": r"$\sin^22\theta_{12}$",
    "sin²θ₁₃": r"$\sin^2\theta_{13}$",
    "sin²θ₁₂": r"$\sin^2\theta_{12}$",
    "sin²2θ₁₂": r"$\sin^22\theta_{12}$",
    "¹³C(α,n)¹⁶O": r"$^{13}{\rm C}(\alpha,n)^{16}{\rm O}$",
    "²⁴¹Am¹³C": r"$^{241}{\rm Am}^{13}{\rm C}$",
    "⁹Li/⁸He": r"$^{9}{\rm Li}/^{8}{\rm He}$",
    "ν̅": r"$\overline{\nu}$",
    "ν": r"$\nu$",
    "α": r"$\alpha$",
    "δ": r"$\delta$",
    "γ": r"$\gamma$",
    "μ": r"$\mu$",
    "σ": r"$\sigma$",
    "π": r"$\pi$",
    "χ²": r"$χ^2$",
    "·": r"$\cdot$",
    "×": r"$\times$",
    "[#": r"[\#",
    " # ": r" \# ",
    "⁻¹": r"$^{-1}$",
    "⁻²": r"$^{-2}$",
    "¹": r"$^1$",
    "²": r"$^2$",
    "³": r"$^3$",
    "⁴": r"$^4$",
    "⁵": r"$^5$",
    "⁶": r"$^6$",
    "⁷": r"$^7$",
    "⁸": r"$^8$",
    "⁹": r"$^9$",
    "⁰": r"$^0$",
    "ᵢ": r"$_i$",
}

exact_substitutions = {
    "U235": r"$^{235}$U",
    "U238": r"$^{238}$U",
    "Pu239": r"$^{239}$Pu",
    "Pu241": r"$^{241}$Pu",
    "acc": r"accidentals",
    "lihe": r"$^{9}{\rm Li}/^{8}{\rm He}$",
    "fastn": r"fast neutrons",
    "alphan": r"$^{13}{\rm C}(α,n)^{16}{\rm O}$",
    "amc": r"$^{241}{\rm Am}^{13}{\rm C}$",
}

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")

    plot = parser.add_mutually_exclusive_group(required=True)
    plot.add_argument("--plot-all", help="plot all the nodes to the folder", metavar="folder")
    plot.add_argument(
        "--plot",
        nargs="+",
        help="plot the nodes in storages",
        metavar=("folder", "storage"),
    )

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
