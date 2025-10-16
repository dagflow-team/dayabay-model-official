# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.2.1] - 2025-10-16

- feature: validate the data version from `data_information.yaml` and use it to determine the `source_type` (data format).
- feature: check that overridden indices exist.
- fix: apply `Abs` transformation to scaled fission fractions.
- chore: minor fixes and updates.

## [1.2.0] - 2025-10-07

- feature: add `detector_selected` index to select detectors for the χ² construction.
- feature: Add `switch_data` method. It can switch model output between real data (`real`) and Asimov (`asimov`).
- feature: Support all the inputs via `uproot` (`ROOT` is supported just as before).
- update: auto detection of source type skip `parameters` directory natively. Docstring was added.

## [1.1.1] - 2025-10-02

- feature: enable uproot only operation (no ROOT required).
- chore: antineutrino spectrum parametrization edges are stored in a text file instead of python.

## [1.1.0] - 2025-09-25

- feature: example scripts.
- chore: automatic data type detection.
- chore: clean data format.

## [1.0.0] - 2025-09-08

- First public PYPI version. The model is based on v1 from [dgm-dayabay-dev](https://github.com/dagflow-team/dgm-dayabay-dev).
