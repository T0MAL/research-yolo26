#!/usr/bin/env python3
"""Validate research repository structure and notebook syntax."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "experiments"
REQUIRED_DIRS = ("results", "checkpoints")


def validate_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"{path.relative_to(ROOT)}: invalid JSON ({error})"]

    if notebook.get("nbformat") != 4:
        errors.append(f"{path.relative_to(ROOT)}: expected notebook format 4")
    cells = notebook.get("cells")
    if not isinstance(cells, list) or not cells:
        errors.append(f"{path.relative_to(ROOT)}: notebook has no cells")
        return errors
    for index, cell in enumerate(cells):
        if cell.get("cell_type") not in {"code", "markdown", "raw"}:
            errors.append(
                f"{path.relative_to(ROOT)}: cell {index} has invalid cell_type"
            )
        if not isinstance(cell.get("source"), list):
            errors.append(
                f"{path.relative_to(ROOT)}: cell {index} source must be a list"
            )
    return errors


def validate_repo() -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    experiments = sorted(path for path in EXPERIMENTS.iterdir() if path.is_dir())

    for directory in experiments:
        match = re.fullmatch(r"(\d{3})_[a-z0-9_]+", directory.name)
        if not match:
            errors.append(
                f"{directory.relative_to(ROOT)}: use NNN_short_description naming"
            )
            continue
        experiment_id = match.group(1)
        if experiment_id in seen_ids:
            errors.append(f"duplicate experiment ID: {experiment_id}")
        seen_ids.add(experiment_id)

        notebook = directory / "experiment.ipynb"
        readme = directory / "README.md"
        if not notebook.is_file():
            errors.append(f"{directory.relative_to(ROOT)}: missing experiment.ipynb")
        else:
            errors.extend(validate_notebook(notebook))
        if not readme.is_file():
            errors.append(f"{directory.relative_to(ROOT)}: missing README.md")
        for name in REQUIRED_DIRS:
            if not (directory / name).is_dir():
                errors.append(f"{directory.relative_to(ROOT)}: missing {name}/")

    if not experiments:
        errors.append("no experiment directories found")
    for required in ("README.md", "JOURNAL.md", ".gitignore"):
        if not (ROOT / required).is_file():
            errors.append(f"missing root {required}")
    return errors


def main() -> int:
    errors = validate_repo()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    count = sum(1 for path in EXPERIMENTS.iterdir() if path.is_dir())
    print(f"Repository valid: {count} experiment(s), all notebooks parse correctly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
