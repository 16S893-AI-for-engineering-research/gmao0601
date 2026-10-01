#!/usr/bin/env python3
"""Recreate and transparently digitize the supplied Peterson conductivity plot.

The values written by this program are sampled from image pixels, not original
measurements.  Pixel calibration and the sampled pixel centre-lines are kept
below and exported with every run for reproducibility.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Plot rectangle in peterson4.6.png, measured in image pixels.  The axes are
# logarithmic: x=10^6 at x=159 and x=10^10 at x=890; y=10^6 at y=48 and
# y=10^-10 at y=728.  The right edge is approximately 5e10 Hz.
X_FIRST_PIXEL, X_FIRST_VALUE = 159.0, 1.0e6
X_SECOND_PIXEL, X_SECOND_VALUE = 890.0, 1.0e10
Y_FIRST_PIXEL, Y_FIRST_VALUE = 48.0, 1.0e6
Y_SECOND_PIXEL, Y_SECOND_VALUE = 728.0, 1.0e-10

# Centre-line samples read from the raster image.  Each tuple is
# (horizontal pixel, vertical pixel); values are therefore necessarily
# approximate to roughly one to two image pixels.
PIXEL_SAMPLES = {
    "41 km": [(160, 49), (200, 52.5), (250, 58), (300, 63.5), (342, 77.5),
              (396, 99.5), (450, 123.5), (525, 158.5), (600, 193.5),
              (707, 243.5), (800, 286.5), (890, 328.5), (950, 357), (1016, 387)],
    "61 km": [(160, 90.5), (200, 95), (250, 100.5), (300, 106.5), (342, 120),
              (396, 142), (450, 166.5), (525, 201), (600, 236.5), (707, 286),
              (800, 329.5), (890, 371.5), (950, 399.5), (1016, 430)],
    "71 km": [(160, 107.5), (200, 112), (250, 117.5), (300, 123.5), (342, 136.5),
              (396, 158.5), (450, 183.5), (525, 218), (600, 253), (707, 303),
              (800, 346.5), (890, 388.5), (950, 416.5), (1016, 447)],
    "81 km": [(160, 176), (200, 180.5), (250, 185.5), (300, 191.5), (342, 205.5),
              (396, 227), (450, 251.5), (525, 286), (600, 321), (707, 371),
              (800, 415), (890, 457), (950, 485), (1016, 515)],
    "100 km": [(160, 231), (200, 236), (250, 241), (300, 247), (342, 260.5),
               (396, 282.5), (450, 307), (525, 342), (600, 377), (707, 426.5),
               (800, 470.5), (890, 512.5), (950, 540.5), (1016, 570.5)],
    "120 km": [(160, 303.5), (200, 308), (250, 313.5), (300, 319.5), (342, 333.5),
               (396, 355), (450, 379.5), (525, 414.5), (600, 449.5), (707, 499.5),
               (800, 542.5), (890, 584.5), (950, 612.5), (1016, 643)],
}
COLORS = {
    "41 km": "#0072bd", "61 km": "#d95319", "71 km": "#edb120",
    "81 km": "#7e2f8e", "100 km": "#77ac30", "120 km": "#4dbeee",
}


def linear_pixel_to_data(pixel, first_pixel, first_value, second_pixel, second_value):
    """Linearly map *pixel* between two calibration points (for linear axes)."""
    return first_value + (pixel - first_pixel) * (second_value - first_value) / (
        second_pixel - first_pixel
    )


def log_pixel_to_data(pixel, first_pixel, first_value, second_pixel, second_value):
    """Map a pixel coordinate through a base-10 logarithmic axis."""
    log_value = linear_pixel_to_data(
        pixel, first_pixel, np.log10(first_value), second_pixel, np.log10(second_value)
    )
    return float(10 ** log_value)


def digitized_series():
    """Return image-derived (frequency Hz, conductivity S/m) samples."""
    result = {}
    for label, samples in PIXEL_SAMPLES.items():
        result[label] = [
            (log_pixel_to_data(px, X_FIRST_PIXEL, X_FIRST_VALUE, X_SECOND_PIXEL, X_SECOND_VALUE),
             log_pixel_to_data(py, Y_FIRST_PIXEL, Y_FIRST_VALUE, Y_SECOND_PIXEL, Y_SECOND_VALUE))
            for px, py in samples
        ]
    return result


def write_csv(path: Path, series):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["x", "y", "altitude_km", "approximate_from_image"])
        for label, points in series.items():
            altitude = label.split()[0]
            for x, y in points:
                writer.writerow([f"{x:.8g}", f"{y:.8g}", altitude, "true"])


def write_metadata(path: Path):
    metadata = {
        "source_figure": "peterson4.6.png",
        "method": "Manual centre-line samples from the supplied raster image; values are approximate.",
        "axes": {"x": {"scale": "log10", "units": "Hz", "calibration_points": [[X_FIRST_PIXEL, X_FIRST_VALUE], [X_SECOND_PIXEL, X_SECOND_VALUE]]},
                 "y": {"scale": "log10", "units": "S/m", "calibration_points": [[Y_FIRST_PIXEL, Y_FIRST_VALUE], [Y_SECOND_PIXEL, Y_SECOND_VALUE]]}},
        "sample_count_per_series": {label: len(points) for label, points in PIXEL_SAMPLES.items()},
    }
    path.write_text(json.dumps(metadata, indent=2) + "\n")


def render(path: Path, series):
    plt.rcParams.update({"font.family": "sans-serif", "font.size": 14})
    fig, ax = plt.subplots(figsize=(9, 7), dpi=120)
    for label, points in series.items():
        values = np.asarray(points)
        ax.plot(values[:, 0], values[:, 1], color=COLORS[label], lw=2.8, label=label)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e6, 5e10)
    ax.set_ylim(1e-10, 1e6)
    ax.set_title("Radio Frequency vs Plasma Conductivity", fontweight="bold", pad=7)
    ax.set_xlabel("Radio Frequency (Hz)")
    ax.set_ylabel("Conductivity (S/m)")
    ax.grid(which="major", color="#dedede", linewidth=1.0)
    ax.grid(which="minor", color="#d5d5d5", linestyle=(0, (1.5, 3)), linewidth=0.9)
    legend = ax.legend(title="Altitude", loc="upper right", frameon=True, fancybox=False,
                       framealpha=1, borderpad=0.35, handlelength=3.0, handletextpad=0.3)
    legend.get_title().set_fontweight("bold")
    fig.subplots_adjust(left=0.148, right=0.942, bottom=0.134, top=0.94)
    fig.savefig(path)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Supplied source image (recorded for validation).")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for derived CSV, JSON, and PNG files.")
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error(f"source image does not exist: {args.source}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    series = digitized_series()
    write_csv(args.output_dir / "peterson4_6_digitized_approximate.csv", series)
    write_metadata(args.output_dir / "peterson4_6_calibration.json")
    render(args.output_dir / "peterson4_6_recreation.png", series)


if __name__ == "__main__":
    main()
