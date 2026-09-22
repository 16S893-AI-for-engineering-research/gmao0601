#!/usr/bin/env python3
"""
Loaded Skill: Figure generator from test_data.csv
Plots time vs number_of_pets and time vs number_of_people from a CSV with headers:
  time,number_of_pets,number_of_people
The script outputs a PNG figure in the same directory by default.
"""

import sys
import os
import csv


def plot_csv(csv_path: str, out_path: str = None) -> int:
    # Import matplotlib lazily; provide a helpful error if unavailable
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        print("Error: Matplotlib is required to generate the figure but is not installed.", file=sys.stderr)
        return 2

    times = []
    pets = []
    people = []

    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found: {csv_path}", file=sys.stderr)
        return 3

    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        # Validate expected columns
        required = {'time', 'number_of_pets', 'number_of_people'}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            print("Error: CSV must have headers: time,number_of_pets,number_of_people", file=sys.stderr)
            return 4
        for row in reader:
            try:
                t = float(row['time'])
                p = float(row['number_of_pets'])
                q = float(row['number_of_people'])
            except Exception:
                continue
            times.append(t)
            pets.append(p)
            people.append(q)

    if not times:
        print("Error: No numeric data found in CSV.", file=sys.stderr)
        return 5

    plt.figure(figsize=(8, 6))
    plt.plot(times, pets, label='number_of_pets', marker='o', linestyle='-')
    plt.plot(times, people, label='number_of_people', marker='x', linestyle='-')
    plt.xlabel('time')
    plt.ylabel('count')
    plt.title(f"Figure from {os.path.basename(csv_path)}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    if not out_path:
        out_path = os.path.splitext(csv_path)[0] + "_figure.png"
    plt.savefig(out_path, dpi=300)
    print(out_path)
    return 0


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Plot a CSV with time, number_of_pets and number_of_people.')
    parser.add_argument('--csv', default='test_data.csv', help='Path to the input CSV file')
    parser.add_argument('--out', default=None, help='Path to save the output PNG figure')
    args = parser.parse_args()

    code = plot_csv(args.csv, args.out)
    sys.exit(code)


if __name__ == '__main__':
    main()
