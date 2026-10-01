"""Acceptance tests for the scientific-figure recreation workflow.

These tests define the public contract for ``assignment2/recreate_plot.py``.
The implementation is deliberately not supplied: run this module with pytest
from the repository root after implementing the recreation script.
"""

import csv
import subprocess
import sys
from pathlib import Path

import pytest


ASSIGNMENT_DIR = Path(__file__).resolve().parents[1]
SOURCE_FIGURE = ASSIGNMENT_DIR / "peterson4.6.png"
SCRIPT = ASSIGNMENT_DIR / "recreate_plot.py"


def run_recreation(output_dir):
    """Run the public CLI against the supplied source figure."""
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--source",
            str(SOURCE_FIGURE),
            "--output-dir",
            str(output_dir),
        ],
        capture_output=True,
        text=True,
    )


def test_source_figure_is_available():
    """The test fixture must remain the supplied Peterson figure."""
    assert SOURCE_FIGURE.is_file()


def test_recreation_cli_exports_transparent_digitized_csv(tmp_path):
    """Digitized values must be exported and explicitly marked approximate."""
    result = run_recreation(tmp_path)

    assert result.returncode == 0, result.stderr
    csv_files = list(tmp_path.glob("*.csv"))
    assert csv_files, "The recreation must export at least one digitized CSV file."

    with csv_files[0].open(newline="") as data_file:
        rows = list(csv.reader(data_file))

    assert len(rows) >= 2, "The digitized CSV must have a header and sampled data."
    header = [column.strip().lower() for column in rows[0]]
    assert "x" in header and "y" in header
    assert any("approx" in column for column in header), (
        "Image-derived values must be labeled approximate in the CSV header."
    )


def test_recreation_cli_writes_calibration_metadata_and_new_plot(tmp_path):
    """A reproducible run records calibration and renders a distinct output image."""
    result = run_recreation(tmp_path)

    assert result.returncode == 0, result.stderr
    metadata_files = list(tmp_path.glob("*.json"))
    plot_files = list(tmp_path.glob("*.png"))

    assert metadata_files, "Save calibration points and transforms as JSON metadata."
    assert plot_files, "Render the recreation as a new PNG image."
    assert all(plot.resolve() != SOURCE_FIGURE.resolve() for plot in plot_files)


@pytest.mark.parametrize(
    "pixel, expected_value",
    [(100, 0.0), (300, 10.0), (200, 5.0)],
)
def test_linear_axis_calibration_maps_known_and_intermediate_ticks(pixel, expected_value):
    """The reusable calibration helper linearly maps pixel coordinates to data."""
    sys.path.insert(0, str(ASSIGNMENT_DIR))
    try:
        from recreate_plot import linear_pixel_to_data
    except ModuleNotFoundError as error:
        pytest.fail("Implement recreate_plot.py with linear_pixel_to_data().")
    finally:
        sys.path.pop(0)

    value = linear_pixel_to_data(
        pixel=pixel,
        first_pixel=100,
        first_value=0.0,
        second_pixel=300,
        second_value=10.0,
    )

    assert value == pytest.approx(expected_value)
