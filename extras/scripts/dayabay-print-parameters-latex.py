#!/usr/bin/env python

"""For each group of parameters create a latex file with information, including
name, description, values and uncertainties.

Note, it was found that having compact tables is easier, thus having a full list of parameters in a
table is avoided.

Usage:
$ ./extras/scripts/dayabay-print-parameters-latex.py output/parameters
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

    storage["parameters.all"].to_latex_files_split(
        opts.output,
        filter_columns=["central", "count"],
        to_latex_kwargs={
            "float_format": "{:.6g}".format,
            "index": False,
        },
        latex_substitutions=latex_substitutions,
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

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument("output", help="print latex tables with parameters")
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
