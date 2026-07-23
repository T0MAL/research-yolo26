# YOLO26 Road-Damage Research

This repository keeps every experiment self-contained and reproducible. One
experiment directory contains one primary notebook, its configuration notes,
and a small results manifest. Large datasets, checkpoints, and generated
outputs stay outside Git.

## Repository layout

```text
.
├── experiments/          # Numbered research experiments
│   └── 001_.../
│       ├── experiment.ipynb
│       ├── README.md
│       ├── results/
│       └── checkpoints/
├── notebooks/templates/  # Source template for new experiment notebooks
├── data/
│   ├── raw/              # Original data (ignored by Git)
│   └── processed/        # Prepared data (ignored by Git)
├── artifacts/            # Shared generated files (ignored by Git)
├── JOURNAL.md             # Chronological research record
├── scripts/               # Experiment creation and validation utilities
└── tests/                 # Repository structure tests
```

## Experiment workflow

1. Create a numbered experiment:

   ```bash
   python scripts/create_experiment.py "short experiment name"
   ```

2. Edit the generated `experiments/NNN_name/experiment.ipynb`.
3. Upload or open it in Colab and run all cells.
4. Download the executed notebook back to the same path.
5. Put small result tables in the experiment's `results/` directory. Keep
   checkpoints and large predictions in Drive or another artifact store.
6. Update the experiment `README.md` and add one row plus a dated entry to
   `JOURNAL.md`.
7. Validate the repository:

   ```bash
   python scripts/validate_repo.py
   python -m unittest discover -s tests
   ```

## Naming and reproducibility rules

- Use `NNN_short_description` for experiment directories.
- Keep one primary notebook named `experiment.ipynb` in each directory.
- Record the hypothesis before running the experiment.
- Record dataset version/location, split, seed, package versions, hardware,
  model/configuration, and exact metrics.
- Do not commit datasets, model weights, secrets, or Colab credentials.
- Prefer CSV/JSON for small results so experiments can be compared later.
- Preserve failed runs in the journal; negative results are research results.

The initial notebook has been registered as experiment
`001_yolo26s_rdd2022_baseline`. The prompt-feasibility follow-up is registered
as `002_yolo26_vs_yoloe26_prompt_feasibility`.
