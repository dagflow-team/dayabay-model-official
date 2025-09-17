#!/usr/bin/env python

"""Plots detector related time dependent data.

Usage:
$ ./extras/scripts/dayabay-plot-detector-data.py -o "output/detector_{type}.pdf"
"""

from __future__ import annotations

from argparse import Namespace

from dag_modelling.tools.logger import set_verbosity
from matplotlib import pyplot as plt
from matplotlib import transforms

from dayabay_model_official import model_dayabay

plt.rcParams.update(
    {
        "axes.grid": False,
        "xtick.minor.visible": True,
        "ytick.minor.visible": True,
    }
)


def main(opts: Namespace) -> None:
    if opts.verbose:
        set_verbosity(opts.verbose)

    model = model_dayabay(source_type=opts.source_type, parameter_values=opts.par)

    storage = model.storage

    days_storage = storage["outputs.daily_data.days"]
    eff_storage = storage["outputs.daily_data.detector.eff"]
    eff_livetime_storage = storage["outputs.daily_data.detector.eff_livetime"]
    rate_accidentals_storage = storage["outputs.daily_data.detector.rate_accidentals"]

    ads = ["AD11", "AD12", "AD21", "AD22", "AD31", "AD32", "AD33", "AD34"]
    ads = {ad: i for i, ad in enumerate(ads)}

    gridspec_kw = {
        "hspace": 0,
        "left": 0.08,
        "right": 0.92,
        "bottom": 0.05,
        "top": 0.95,
    }
    figsize = (12, 10)
    fig_eff, axes_eff = plt.subplots(
        8,
        1,
        sharex=True,
        figsize=figsize,
        subplot_kw={"ylabel": r"$\varepsilon$, %"},
        gridspec_kw=gridspec_kw,
    )
    fig_eff_livetime, axes_eff_livetime = plt.subplots(
        8,
        1,
        sharex=True,
        figsize=figsize,
        subplot_kw={"ylabel": r"T, day"},
        gridspec_kw=gridspec_kw,
    )
    fig_rate_accidentals, axes_rate_accidentals = plt.subplots(
        8,
        1,
        sharex=True,
        figsize=figsize,
        subplot_kw={"ylabel": r"R, #/day"},
        gridspec_kw=gridspec_kw,
    )
    text_offset = transforms.ScaledTranslation(0.04, 0.04, fig_eff.dpi_scale_trans)

    axes_eff[0].set_title("Efficiency (muon veto, multiplicity)")
    axes_eff_livetime[0].set_title("Effective livetime")
    axes_rate_accidentals[0].set_title("Accidentals rate")

    labels_added = set()

    seconds_in_day = 60 * 60 * 24
    plot_kwargs = dict(markersize=0.5, color="C0")
    for (period, ad), output in eff_storage.walkitems():
        data_days = days_storage[period].data
        eff_data = output.data
        eff_livetime_data = eff_livetime_storage[period, ad].data
        rate_accidentals_data = rate_accidentals_storage[period, ad].data

        ad_id = ads[ad]

        ax_eff = axes_eff[ad_id]
        mask = eff_data > 0
        ax_eff.plot(data_days[mask], eff_data[mask] * 100, ".", **plot_kwargs)

        ax_eff_livetime = axes_eff_livetime[ad_id]
        mask = eff_livetime_data > 0
        ax_eff_livetime.plot(
            data_days[mask], eff_livetime_data[mask] / seconds_in_day, ".", **plot_kwargs
        )

        ax_rate_accidentals = axes_rate_accidentals[ad_id]
        mask = rate_accidentals_data > 0
        ax_rate_accidentals.plot(data_days[mask], rate_accidentals_data[mask], ".", **plot_kwargs)

        ticks_right = bool(ad_id % 2)
        for ax in (ax_eff, ax_eff_livetime, ax_rate_accidentals):
            if ad not in labels_added:
                ax.text(1, 1, ad, transform=ax.transAxes - text_offset, va="top", ha="right")
                labels_added.add(ad)

            ax.tick_params(
                axis="y",
                which="both",
                left=not ticks_right,
                right=ticks_right,
                labelleft=not ticks_right,
                labelright=ticks_right,
            )
            if ticks_right:
                ax.yaxis.set_label_position("right")

        labels_added.add(ad)

    for axes in (axes_eff, axes_eff_livetime, axes_rate_accidentals):
        ax = axes[-1]
        ax.set_xlabel("Day since start of data taking")
        ax.set_xlim(left=0)

    if opts.output:
        for plot_type, fig in {
            "eff": fig_eff,
            "eff_livetime": fig_eff_livetime,
            "rate_accidentals": fig_rate_accidentals,
        }.items():
            if "{type" not in opts.output:
                raise RuntimeError("Output format should contain {type} for plot type")

            fname = opts.output.format(type=plot_type)
            fig.savefig(fname)
            print(f"Save plot: {fname}")

    if opts.show or not opts.output:
        plt.show()


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Plot time dependent detector data")
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument(
        "--source-type",
        choices=("tsv", "hdf5", "root", "npz"),
        default="default:hdf5",
        help="Data source type",
    )

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    plot = parser.add_argument_group("pars", "plots")
    plot.add_argument(
        "-o",
        "--output",
        help='output files (supported format keys: "type", "selection")',
    )
    plot.add_argument("-s", "--show", action="store_true", help="show")

    main(parser.parse_args())
