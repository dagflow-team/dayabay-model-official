#!/usr/bin/env python

"""Saves subgraphs around each node.

For a given node two previous layers are shown (up to depth -2) and one

Usage:
- Walk through the storage of nodes and plot a subgraph for each node.
$ ./extras/scripts/dayabay-plot-all-subgraphs.py --graphs-all output/dayabay_graphs
- Walk through the storage of nodes, starting from 'detector' and plot a subgraph for each node.
$ ./extras/scripts/dayabay-plot-all-subgraphs.py --graphs output/dayabay_graphs detector
"""

from __future__ import annotations

from argparse import Namespace
from contextlib import suppress
from pathlib import Path

from dag_modelling.tools.logger import set_verbosity

from dayabay_model_official import model_dayabay


def main(opts: Namespace) -> None:
    if opts.verbose:
        set_verbosity(opts.verbose)

    model = model_dayabay(path_data=opts.path_data, parameter_values=opts.par)
    storage = model.storage

    graph_accept_index = {
        "reactor": [0],
        "detector": [0, 1],
        "isotope": [0],
        "period": [1, 2],
    }
    if opts.graphs_all:
        path = Path(opts.graphs_all)
        storage["parameter_group.all"].savegraphs(
            path / "parameters",
            min_depth=opts.min_depth,
            max_depth=opts.max_depth,
            keep_direction=True,
            show="all",
            accept_index=graph_accept_index,
            filter=graph_accept_index,
        )
        with suppress(KeyError):
            storage["parameters.sigma"].savegraphs(
                path / "parameters" / "sigma",
                min_depth=opts.min_depth,
                max_depth=opts.max_depth,
                keep_direction=True,
                show="all",
                accept_index=graph_accept_index,
                filter=graph_accept_index,
            )
        storage["nodes"].savegraphs(
            path,
            min_depth=opts.min_depth,
            max_depth=opts.max_depth,
            keep_direction=True,
            show="all",
            accept_index=graph_accept_index,
            filter=graph_accept_index,
        )

    if opts.graphs:
        folder, *nodepaths = opts.graphs
        folder = Path(folder)
        for nodepath in nodepaths:
            nodes = storage("nodes")[nodepath]
            nodes.savegraphs(
                f"{folder}/{nodepath.replace('.', '/')}",
                min_depth=opts.min_depth,
                max_depth=opts.max_depth,
                keep_direction=True,
                show="all",
                accept_index=graph_accept_index,
                filter=graph_accept_index,
            )


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Plot a subgraph with graphviz around each node")
    parser.add_argument("-v", "--verbose", default=1, action="count", help="verbosity level")
    parser.add_argument(
        "--path-data",
        default=None,
        help="Path to data",
    )

    dot = parser.add_argument_group("graphviz", "plotting graphs")
    dot.add_argument("--min-depth", "--md", default=-2, type=int, help="minimal depth")
    dot.add_argument("--max-depth", "--Md", default=+1, type=int, help="maximaldepth depth")
    dot.add_argument("--graphs-all", help="plot graphs", metavar="folder")
    dot.add_argument(
        "--graphs",
        nargs="+",
        help="save partial graphs from every node",
        metavar=("folder", "storage"),
    )

    pars = parser.add_argument_group("pars", "setup pars")
    pars.add_argument("--par", nargs=2, action="append", default=[], help="set parameter value")

    main(parser.parse_args())
