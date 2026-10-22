#!/usr/bin/env python3
"""Generate an SVG dependency diagram from the current Backlog task workflow."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path


@dataclass(frozen=True)
class Task:
    task_id: str
    lines: tuple[str, ...]
    x: int
    y: int
    status: str = "todo"
    tag: str = ""


WIDTH = 1700
HEIGHT = 1940
CARD_W = 360
CARD_H = 112
OUT = Path(__file__).with_name("backlog-workflow.svg")

TASKS = (
    Task("TASK-3", ("Summarize US3D manuals", "by chapter"), 60, 270, "done", "reference"),
    Task("TASK-1.1", ("Inventory necessary and available", "US3D reference materials"), 470, 270, "ready", "start here"),
    Task("TASK-2", ("Build evidence-backed US3D", "hook-selection subagent"), 880, 270, "progress", "supporting track"),
    Task("TASK-1.14", ("Describe the target", "simulation problem"), 1290, 270, "ready", "user input"),
    Task("TASK-1.12", ("Create plugin-writing", "reference guide and skill"), 150, 485, "todo", "guide"),
    Task("TASK-1.13", ("Create input-file-writing", "reference guide and skill"), 560, 485, "todo", "guide"),
    Task("TASK-1.2", ("Document user-selected equations", "and calculation order"), 1130, 485, "todo", "user input"),
    Task("TASK-1.3", ("Identify candidate US3D hooks", "for approved equations"), 850, 700, "todo", "evidence gate"),
    Task("TASK-1.4", ("Initialize supported hooks and", "plugin variables without physics"), 650, 900, "todo", "build"),
    Task("TASK-1.15", ("Verify initialized plugin leaves", "the simulation unchanged"), 850, 1100, "todo", "external US3D"),
    Task("TASK-1.5", ("Implement user-supplied equations", "one task per equation"), 850, 1290, "todo", "split later"),
    Task("TASK-1.9", ("Verify coupled plugin with", "canonical cases—one per case"), 850, 1450, "todo", "external US3D"),
    Task("TASK-1.10", ("Compare no-field and applied-field", "hypersonic cases"), 850, 1600, "todo", "application"),
    Task("TASK-1.16", ("Assess sensitivity of", "hypersonic results"), 440, 1760, "todo", "split later"),
    Task("TASK-1.11", ("Consolidate documentation and", "assess release readiness"), 850, 1760, "todo", "release gate"),
)

# Solid arrows are direct Backlog dependencies. The one dashed arrow is advisory.
EDGES = (
    ("TASK-3", "TASK-1.12", False),
    ("TASK-3", "TASK-1.13", False),
    ("TASK-1.1", "TASK-1.12", False),
    ("TASK-1.1", "TASK-1.13", False),
    ("TASK-1.1", "TASK-1.3", False),
    ("TASK-1.14", "TASK-1.2", False),
    ("TASK-1.14", "TASK-1.15", False),
    ("TASK-1.14", "TASK-1.10", False),
    ("TASK-1.2", "TASK-1.3", False),
    ("TASK-1.2", "TASK-1.5", False),
    ("TASK-2", "TASK-1.3", True),
    ("TASK-1.12", "TASK-1.4", False),
    ("TASK-1.3", "TASK-1.4", False),
    ("TASK-1.4", "TASK-1.15", False),
    ("TASK-1.13", "TASK-1.15", False),
    ("TASK-1.15", "TASK-1.5", False),
    ("TASK-1.13", "TASK-1.9", False),
    ("TASK-1.5", "TASK-1.9", False),
    ("TASK-1.9", "TASK-1.10", False),
    ("TASK-1.10", "TASK-1.16", False),
    ("TASK-1.16", "TASK-1.11", False),
)

COLORS = {
    "done": ("#D9F5E5", "#26734D", "#17563A"),
    "progress": ("#FFF0BF", "#BE7B00", "#764D00"),
    "ready": ("#DCEFFF", "#1C7CAE", "#145F86"),
    "todo": ("#FFFFFF", "#8AA5B5", "#263842"),
}


def card(task: Task) -> str:
    fill, stroke, ink = COLORS[task.status]
    status_text = {
        "done": "DONE",
        "progress": "IN PROGRESS",
        "ready": "READY NOW",
        "todo": "TO DO",
    }[task.status]
    text_lines = "".join(
        f'<text class="task-title" x="{task.x + 20}" y="{task.y + 61 + i * 25}">{escape(line)}</text>'
        for i, line in enumerate(task.lines)
    )
    return f"""
    <g id="{task.task_id.replace('.', '-')}">
      <rect class="card-shadow" x="{task.x + 2}" y="{task.y + 5}" width="{CARD_W}" height="{CARD_H}" rx="14"/>
      <rect class="card" x="{task.x}" y="{task.y}" width="{CARD_W}" height="{CARD_H}" rx="14"
            fill="{fill}" stroke="{stroke}"/>
      <text class="task-id" x="{task.x + 20}" y="{task.y + 27}" fill="{ink}">{task.task_id}</text>
      <rect x="{task.x + 220}" y="{task.y + 12}" width="120" height="24" rx="12" fill="{stroke}"/>
      <text class="status" x="{task.x + 280}" y="{task.y + 29}">{status_text}</text>
      {text_lines}
      <text class="tag" x="{task.x + 340}" y="{task.y + 99}" text-anchor="end">{escape(task.tag)}</text>
    </g>"""


def edge(source: Task, target: Task, dashed: bool) -> str:
    x1, y1 = source.x + CARD_W / 2, source.y + CARD_H
    x2, y2 = target.x + CARD_W / 2, target.y
    gap = y2 - y1
    bend = max(35, gap * 0.48)
    dash = ' stroke-dasharray="10 8"' if dashed else ""
    marker = "arrow-advisory" if dashed else "arrow"
    return (
        f'<path class="edge{" advisory" if dashed else ""}" '
        f'd="M {x1:g} {y1:g} C {x1:g} {y1 + bend:g}, {x2:g} {y2 - bend:g}, {x2:g} {y2:g}"'
        f'{dash} marker-end="url(#{marker})"/>'
    )


def main() -> None:
    by_id = {task.task_id: task for task in TASKS}
    arrows = "\n    ".join(edge(by_id[a], by_id[b], dashed) for a, b, dashed in EDGES)
    cards = "\n".join(card(task) for task in TASKS)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">Backlog workflow for the US3D plasma and MHD plugin project</title>
  <desc id="desc">Dependency diagram for TASK-1 and its supporting backlog tasks. Solid arrows mean required dependencies; a dashed arrow means optional support.</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#56798B"/>
    </marker>
    <marker id="arrow-advisory" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#BE7B00"/>
    </marker>
    <style>
      .card-shadow {{ fill: #12394D; opacity: 0.12; }}
      .card {{ stroke-width: 2.5; }}
      .edge {{ fill: none; stroke: #56798B; stroke-width: 3; opacity: 0.76; }}
      .edge.advisory {{ stroke: #BE7B00; opacity: 0.9; }}
      .task-id {{ font: 700 18px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
      .task-title {{ font: 600 19px Georgia, "Times New Roman", serif; fill: #172A34; }}
      .status {{ font: 700 10px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: white; text-anchor: middle; letter-spacing: .5px; }}
      .tag {{ font: italic 13px Georgia, "Times New Roman", serif; fill: #536D79; }}
      .phase {{ font: 700 15px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #145F86; letter-spacing: 1.3px; }}
      .legend {{ font: 15px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #314A57; }}
    </style>
  </defs>
  <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="#F5FAFD"/>
  <path d="M0 0 H1700 V175 Q1300 120 900 165 T0 145 Z" fill="#D8F0FC"/>
  <text x="60" y="65" font-family="Georgia, 'Times New Roman', serif" font-size="38" font-weight="700" fill="#12394D">US3D Plugin Backlog Workflow</text>
  <text x="60" y="102" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="18" fill="#3F6273">TASK-1: plasma and MHD plugin for magnetic-window studies</text>
  <g transform="translate(980 48)">
    <circle cx="0" cy="0" r="8" fill="#26734D"/><text class="legend" x="16" y="5">Done</text>
    <circle cx="95" cy="0" r="8" fill="#BE7B00"/><text class="legend" x="111" y="5">In progress</text>
    <circle cx="230" cy="0" r="8" fill="#1C7CAE"/><text class="legend" x="246" y="5">Ready now</text>
    <circle cx="360" cy="0" r="8" fill="#8AA5B5"/><text class="legend" x="376" y="5">To do</text>
    <line x1="0" y1="38" x2="54" y2="38" stroke="#56798B" stroke-width="3" marker-end="url(#arrow)"/><text class="legend" x="66" y="43">required dependency</text>
    <line x1="255" y1="38" x2="309" y2="38" stroke="#BE7B00" stroke-width="3" stroke-dasharray="10 8" marker-end="url(#arrow-advisory)"/><text class="legend" x="321" y="43">optional support</text>
  </g>

  <rect x="35" y="205" width="1630" height="205" rx="20" fill="#EAF6FC"/>
  <text class="phase" x="60" y="235">FOUNDATIONS — CURRENT ENTRY POINTS</text>
  <rect x="35" y="440" width="1630" height="185" rx="20" fill="#EFF8F3"/>
  <text class="phase" x="60" y="470">GUIDES + PROBLEM DEFINITION</text>
  <rect x="35" y="655" width="1630" height="550" rx="20" fill="#F3F0FA"/>
  <text class="phase" x="60" y="685">HOOK SELECTION + SAFE INITIALIZATION</text>
  <rect x="35" y="1245" width="1630" height="170" rx="20" fill="#FFF8E7"/>
  <text class="phase" x="60" y="1275">EQUATION IMPLEMENTATION</text>
  <rect x="35" y="1425" width="1630" height="475" rx="20" fill="#F9F1F3"/>
  <text class="phase" x="60" y="1445">VERIFICATION + APPLICATION + RELEASE</text>

  <g aria-label="Dependency arrows">
    {arrows}
  </g>
  <g aria-label="Backlog tasks">
{cards}
  </g>
  <text x="60" y="1918" class="legend">Snapshot generated from Backlog tasks • solid lines show direct dependencies • TASK-1.5, TASK-1.9, TASK-1.16, and TASK-1.11 are planning placeholders to split later</text>
</svg>
"""
    OUT.write_text(svg, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
