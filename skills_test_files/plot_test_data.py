#!/usr/bin/env python3
"""Create a publication-ready line plot from test_data.csv."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def load_data(csv_path: Path) -> tuple[list[float], list[float], list[float]]:
    """Load and validate the expected columns from the input CSV."""
    time: list[float] = []
    pets: list[float] = []
    people: list[float] = []
    required_columns = {"time", "number_of_pets", "number_of_people"}

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            missing = required_columns.difference(reader.fieldnames or [])
            raise ValueError(f"Missing required CSV columns: {', '.join(sorted(missing))}")

        for line_number, row in enumerate(reader, start=2):
            try:
                time.append(float(row["time"]))
                pets.append(float(row["number_of_pets"]))
                people.append(float(row["number_of_people"]))
            except (TypeError, ValueError) as error:
                raise ValueError(f"Invalid numeric value on CSV line {line_number}") from error

    if not time:
        raise ValueError("The CSV contains no data rows")

    return time, pets, people


def make_figure(csv_path: Path, output_path: Path) -> None:
    """Plot both data series and save the result as a JPEG."""
    try:
        import matplotlib as mpl
        import matplotlib.pyplot as plt
    except ImportError as error:
        raise SystemExit(
            "Matplotlib is required. Install it with: python3 -m pip install matplotlib"
        ) from error

    time, pets, people = load_data(csv_path)

    # Helvetica is preferred; the remaining entries are portable fallbacks.
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
            "font.size": 28,
            "axes.labelsize": 28,
            "xtick.labelsize": 28,
            "ytick.labelsize": 28,
            "legend.fontsize": 28,
        }
    )

    fig, ax = plt.subplots(figsize=(12, 8))
    # No explicit colors: each line uses Matplotlib's default color cycle.
    ax.plot(time, pets, linewidth=2.5, label="Number of pets")
    ax.plot(time, people, linewidth=2.5, label="Number of people")
    ax.set_xlabel("Time")
    ax.set_ylabel("Count")
    ax.legend(frameon=False)
    ax.margins(x=0)

    fig.tight_layout(pad=0.5)
    fig.savefig(
        output_path,
        format="jpeg",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.05,
    )
    plt.close(fig)


def main() -> None:
    script_directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=script_directory / "test_data.csv",
        help="input CSV (default: test_data.csv beside this script)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=script_directory / "test_data_figure.jpeg",
        help="output JPEG path (default: test_data_figure.jpeg beside this script)",
    )
    args = parser.parse_args()

    make_figure(args.input.resolve(), args.output.resolve())
    print(f"Saved figure to {args.output.resolve()}")


if __name__ == "__main__":
    main()
