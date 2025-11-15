#!/usr/bin/env python

"""Saves the memory buffer of each output in the storage to the root file,
preserving the location structure.

Usage:
- Save the outputs the file of a choice:
$ ./extras/scripts/dayabay-save-outputs-to-root.py output/dayabay.root

Adding `-v` will print information on what is being saved.
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

    storage("outputs").to_root(
        opts.output,
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

    parser = ArgumentParser(description="Save array (graph/histogram) from each output to a root file")
    parser.add_argument("output", help="Export outputs as graphs and histograms to the ROOT file")

    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument(
        "--path-data",
        default=None,
        help="Path to data",
    )

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
