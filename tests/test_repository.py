"""Tests for experiment creation primitives and repository integrity."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


create_experiment = load_module(
    "create_experiment", ROOT / "scripts" / "create_experiment.py"
)
validate_repo = load_module("validate_repo", ROOT / "scripts" / "validate_repo.py")


class RepositoryTests(unittest.TestCase):
    def test_repository_layout_and_notebooks(self) -> None:
        self.assertEqual(validate_repo.validate_repo(), [])

    def test_slugify(self) -> None:
        self.assertEqual(
            create_experiment.slugify("YOLO26: Larger Images!"),
            "yolo26_larger_images",
        )

    def test_empty_slug_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            create_experiment.slugify("---")

    def test_result_manifest_template_exists(self) -> None:
        self.assertTrue(
            (ROOT / "notebooks" / "templates" / "results_README.md").is_file()
        )


if __name__ == "__main__":
    unittest.main()
