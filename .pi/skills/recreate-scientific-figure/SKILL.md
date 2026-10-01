---
name: recreate-scientific-figure
description: Digitize and recreate a scientific plot from a user-supplied paper or figure image: calibrate axes, extract plotted lines and points, export approximate data, and render a reproducible matching figure.
---

# Recreate Scientific Figure

## When to use this
Use this skill when the user supplies a paper, PDF, or figure image and wants a plot recreated, including its curves, markers, error bars, and layout. This is a reproducible, script-based alternative to a tool such as WebPlotDigitizer: extracted values are estimates unless the original numerical data is supplied.

## Steps
1. **Inspect the source and select the target figure.** Read the supplied paper or image and identify the requested figure and panel(s). Record the caption, axis labels and units, plot bounds, linear or logarithmic scales, axis limits and ticks, series-to-legend mapping, line and marker styles, error bars, annotations, and panel layout. Ask the user to resolve unreadable or ambiguous details before digitizing.
2. **Calibrate the plot coordinates.** Locate the pixel coordinates of at least two known ticks on each axis and map image coordinates to data coordinates. Use the appropriate transform for each axis:
   - linear axes: interpolate between calibrated values;
   - logarithmic axes: interpolate in log space before converting back;
   - categorical axes: map each category location explicitly.
   Record calibration points and transforms in the script or a companion data file so results are repeatable.
3. **Extract each series.** Identify series by their color, line style, marker shape, and legend label. Trace or sample the center of each visible line across the plot, avoiding axes, legend samples, labels, and overlapping series. Convert the sampled pixel locations to data coordinates with the calibration transform. Capture discrete markers and error-bar endpoints separately when present. If curves overlap or are obscured, extract only defensible points and mark the gaps rather than inventing data.
4. **Save transparent digitized data.** Export one CSV or other plain-text data file per panel or series, with clear column names and units. Preserve the sampled points, calibration metadata, source figure/page, and any manual assumptions. Clearly label every value derived from an image as approximate; do not represent digitized data as the paper's original data.
5. **Render a reproducible recreation.** Write a standalone plotting script that loads the extracted data and recreates the panel layout, scales, limits, ticks, labels, legend, line/marker styles, error bars, and annotations. Match the source figure's visual hierarchy while keeping all style settings explicit. Generate a new image file rather than editing or copying the source image.
6. **Validate and report.** Run the script and compare its output with the source: verify axes/calibration, line shapes, intersections, marker positions, error bars, series identities, and panel geometry. State the output paths, extraction method, estimated accuracy or limitations, unresolved/occluded regions, and commands used to create the result.

## Notes
Treat this as scientific data digitization, not exact recovery. Image resolution, compression, line thickness, and overlapping curves limit accuracy; request the authors' source data when numerical precision is important. Never fabricate unseen portions of a curve, alter the paper's conclusions, remove watermarks or attribution, or claim the extracted data are original measurements. Retain citation and attribution for the source paper in the recreation when appropriate.
