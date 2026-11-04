# Experiments

Additional runs supplied as a PDF are indexed in the
[reported run archive](../records/README.md), with CSV metrics and source
provenance. They have no accompanying executed notebooks and therefore use
separate record IDs rather than new numbered experiment directories. Their
status is **reported in PDF**, not independently reproduced.

Each numbered directory is a research unit with one primary notebook and an
evidence record:

```text
NNN_short_description/
├── experiment.ipynb     # Source plus retained execution output
├── README.md            # Question, setup, status, evidence, limitations
├── results/             # Compact CSV/JSON results and a manifest
└── checkpoints/         # Model weights; ignored by Git
```

## Status meanings

- **Completed:** the recorded evidence passed basic consistency checks.
- **Interrupted:** execution stopped before the primary comparison completed.
- **Invalidated:** an internal contradiction or provenance problem prevents the
  output from supporting a scientific claim.
- **Setup failed:** execution did not progress beyond environment preparation.

Create a directory with
`python scripts/create_experiment.py "name"`. Do not copy an old experiment:
the template reduces accidental carry-over of paths, outputs, and assumptions.
Keep failed work, but explain why it is non-evidence and what a valid rerun must
change.
