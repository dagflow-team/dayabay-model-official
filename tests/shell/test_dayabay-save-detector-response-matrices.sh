#!/usr/bin/env bash

./extras/scripts/dayabay-save-detector-response-matrices.py --output output/matrix.tsv \
                                                                     output/matrix.npz \
                                                                     output/matrix.hdf5 \
                                                            --plot-output output/matrix{}.pdf

