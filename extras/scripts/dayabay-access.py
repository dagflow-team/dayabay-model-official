#!/usr/bin/env python

"""Demonstrate how to access some of the Daya Bay data from the model:
- Parameter (sin²2θ₁₃) and its value.
- Expected IBD events ad AD11 (EH1AD1).
- Statistic (combined Neyman-Pearson χ²) versus Asimov dataset.
- Plot expected IBD events for different sin²2θ₁₃ values.
- Plot statistic for different sin²2θ₁₃ values.

Usage:
$ ./extras/scripts/dayabay-access.py --show
"""

from __future__ import annotations

from argparse import Namespace

from dag_modelling.tools.logger import set_verbosity
from matplotlib import pyplot as plt
from numpy import linspace, zeros_like

from dayabay_model_official import model_dayabay


def main(opts: Namespace) -> None:
    if opts.verbose:
        set_verbosity(opts.verbose)

    model = model_dayabay(path_data=opts.path_data, parameter_values=opts.par)
    storage = model.storage

    theta13 = storage["parameters.all.survival_probability.SinSq2Theta13"]
    print(f"Initial sin²2θ₁₃={theta13.value}")
    theta13_initial_value = theta13.value
    theta13.push()
    print("Compute covariance matrix. This will take less than a minute...")
    model.update_covariance_matrix()
    model.update_frozen_nodes()

    location = "outputs.eventscount.final.detector"
    print(f"Available outputs at {location}:", list(storage[location].keys()))
    ibd_AD11_output = storage["outputs.eventscount.final.detector.AD11"]
    chi2 = storage[("outputs", "statistic", "stat", "chi2cnp")]

    plt.figure()
    ax = plt.subplot(
        111,
        xlabel="Reconstructed prompt energy",
        ylabel="Expected events",
        title="Expected IBD spectrum at EH1AD1",
    )

    for value in (0.0, 0.08, 0.2):
        theta13.value = value
        ax.plot(ibd_AD11_output.data.copy(), "+", label=f"{value}")
    ax.legend(title="sin²2θ₁₃")

    th13_values = linspace(0.0, 0.2, 200)
    chi2_values = zeros_like(th13_values)
    for i, th13 in enumerate(th13_values):
        theta13.value = th13
        chi2_values[i] = chi2.data[0]

    plt.figure()
    ax = plt.subplot(
        111,
        xlabel=r"$\sin^22\theta_{13}$",
        ylabel=r"$\chi^2$",
        title=r"Combined Neyman-Pearson's $\chi^2$",
    )
    ax.plot(th13_values, chi2_values)
    ax.axvline(theta13_initial_value)

    theta13.pop()
    print(f"Restored sin²2θ₁₃={theta13.value}")

    if opts.show:
        plt.show()


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Print Daya Bay summary")
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument(
        "-s",
        "--show",
    )
    parser.add_argument(
        "--path-data",
        default=None,
        help="Path to data",
    )

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
