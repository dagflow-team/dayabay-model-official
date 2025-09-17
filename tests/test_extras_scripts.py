import os
import subprocess


def run_script(script: str) -> tuple[str, str, int]:
    print("Starting the test of the following script: ", script)
    result = subprocess.run(
        [script],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode(), result.stderr.decode(), result.returncode


def test_run_dayabay_plot_all_nodes():
    output_path = "output/background_plots"
    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-plot-all-outputs-2.sh",
    )

    assert code == 0
    assert stderr == ""
    assert f"Write: {output_path}" in stdout
    assert os.path.exists(output_path)


def test_run_dayabay_plot_subgraph():
    output_path = "output/dayabay_graphs"
    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-plot-all-subgraphs-2.sh",
    )

    assert code == 0
    assert stderr == ""
    assert f"Write: {output_path}" in stdout
    assert os.path.exists(output_path)


def test_run_dayabay_plot_detector_data():
    output = "output/detector_{type}.pdf"

    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-plot-detector-data.sh",
    )

    assert code == 0
    assert stderr == ""
    for type in ["eff", "eff_livetime", "rate_accidentals"]:
        assert f"Save plot: {output.format(type=type)}" in stdout
        assert os.path.exists(output.format(type=type))


def test_run_dayabay_plot_reactor_data():
    output = "output/reactor_{type}.pdf"

    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-plot-reactor-data.sh",
    )

    assert code == 0
    assert stderr == ""
    for type in ["power", "fission_fraction"]:
        assert f"Save plot: {output.format(type=type)}" in stdout
        assert os.path.exists(output.format(type=type))


def test_run_dayabay_print_internal_data():
    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-print-internal-data-3.sh",
    )

    assert code == 0
    assert stderr == ""
    assert "parameters.free" in stdout
    assert "parameters.constrained" in stdout


def test_run_dayabay_print_parameters_latex():
    output_path = "output/parameters"
    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-print-parameters-latex.sh",
    )

    assert code == 0
    assert stderr == ""
    assert os.path.exists(output_path)


def test_run_dayabay_print_parameters_text():
    output_path = "output/parameters.txt"
    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-print-parameters-text.sh",
    )

    assert code == 0
    assert stderr == ""
    assert os.path.exists(output_path)


def test_run_dayabay_print_summary():
    output_paths = [
        "output/dayabay_summary.tsv",
        "output/dayabay_summary.tsv.bz2",
        "output/dayabay_summary.npz",
        "output/dayabay_summary.hdf5"
    ]
    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-print-summary.sh",
    )

    assert code == 0
    assert stderr == ""
    for output_path in output_paths:
        assert os.path.exists(output_path)


def test_run_dayabay_save_detector_response_matrices():
    output_data_path = "output/matrix.{ext}"
    output_plot_path = "output/matrix_{type}.pdf"
    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-save-detector-response-matrices.sh",
    )

    assert code == 0
    assert stderr == ""
    for ext in ["tsv", "npz", "hdf5"]:
        assert os.path.exists(output_data_path.format(ext=ext))

    for type in ["iav", "lsnl", "eres", "total"]:
        assert os.path.exists(output_plot_path.format(type=type))


def test_run_dayabay_save_parameters_to_latex():
    output_path = "output/dayabay_parameters_datax.tex"
    stdout, stderr, code = run_script(
        "./tests/shell/test_dayabay-save-parameters-to-latex.sh",
    )

    assert code == 0
    assert stderr == ""
    assert os.path.exists(output_path)
