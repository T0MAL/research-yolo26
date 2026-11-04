#!/usr/bin/env python3
"""Create the next numbered, self-contained experiment directory."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "experiments"
TEMPLATES = ROOT / "notebooks" / "templates"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    if not slug:
        raise ValueError("experiment name must contain at least one letter or number")
    return slug


def next_id() -> str:
    ids = [
        int(path.name[:3])
        for path in EXPERIMENTS.iterdir()
        if path.is_dir() and re.fullmatch(r"\d{3}_.+", path.name)
    ]
    return f"{max(ids, default=0) + 1:03d}"


def render(source: Path, destination: Path, values: dict[str, str]) -> None:
    text = source.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    destination.write_text(text, encoding="utf-8")


def create_experiment(name: str) -> Path:
    experiment_id = next_id()
    destination = EXPERIMENTS / f"{experiment_id}_{slugify(name)}"
    destination.mkdir()
    (destination / "results").mkdir()
    (destination / "checkpoints").mkdir()

    values = {"ID": experiment_id, "TITLE": name.strip()}
    render(TEMPLATES / "experiment.ipynb", destination / "experiment.ipynb", values)
    render(TEMPLATES / "README.md", destination / "README.md", values)
    render(
        TEMPLATES / "results_README.md",
        destination / "results" / "README.md",
        values,
    )
    (destination / "checkpoints" / ".gitkeep").touch()

    # Fail immediately if a template edit ever produces malformed JSON.
    json.loads((destination / "experiment.ipynb").read_text(encoding="utf-8"))
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help='short name, e.g. "larger input resolution"')
    args = parser.parse_args()
    try:
        destination = create_experiment(args.name)
    except (FileExistsError, ValueError) as error:
        parser.error(str(error))
    print(destination.relative_to(ROOT))
    print("Next: write the hypothesis in README.md and experiment.ipynb.")


if __name__ == "__main__":
    main()
