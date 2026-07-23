# Experiments

Each numbered directory is one research unit with one primary notebook:

```text
NNN_short_description/
├── experiment.ipynb     # Colab notebook; save executed output back here
├── README.md            # Hypothesis, setup, result summary, conclusion
├── results/             # Small CSV/JSON/plots suitable for Git
└── checkpoints/         # Model weights; ignored by Git
```

Create directories with `python scripts/create_experiment.py "name"` instead
of copying an old experiment. The clean template reduces accidental carry-over
of paths, outputs, and assumptions.
