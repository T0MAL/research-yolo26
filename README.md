# YOLO26 Road-Damage Detection Research

An experiment-driven study of YOLO26 for road-damage detection on RDD2022.
The repository documents baseline training, dataset and split auditing, error
decomposition, prompt-aware detection, semantic prototypes, and head-level
ablation design. Completed results, interrupted runs, and invalidated outputs
are labeled separately so that exploratory evidence is not mistaken for a
paper result.

## Research questions

- Which failure mode limits the baseline: geometry, localization,
  classification, or background confusion?
- Do elongated crack boxes need a specialized geometric component?
- Can semantic prompts or visual-language prototypes improve class decisions?
- What controls are required to separate semantic gains from pretraining,
  architecture, and training-budget effects?

## Verified findings

The canonical YOLO26s checkpoint was evaluated on the RDD2022 China test split
in [experiment 003](experiments/003_yolo26s_baseline_error_diagnostics/):

| Metric | Result |
|---|---:|
| Test objects | 893 |
| mAP50 | 0.8453 |
| mAP50–95 | 0.5802 |
| Precision | 0.8563 |
| Recall | 0.7992 |
| Classification accuracy given localization | 0.9897 |

At a diagnostic confidence threshold of 0.05, high-aspect-ratio objects had a
lower miss rate than compact objects: 10.62% for `AR >= 8` versus 16.60% for
`AR < 2`. This does not support thin-object geometry as the first component to
modify. Only 8 of 777 localized objects had the wrong class. The next
evidence-backed direction is therefore confidence calibration and inspection
of crack-like background candidates, followed by a controlled hard-negative
or background-aware loss experiment if the pattern persists.

The 728 unmatched predictions from that analysis are deliberately
low-threshold diagnostic candidates, not the model's official false-positive
rate.

## Experiment map

| ID | Experiment | Status | Evidence or outcome |
|---:|---|---|---|
| 001 | [YOLO26s RDD2022 baseline](experiments/001_yolo26s_rdd2022_baseline/) | Completed checkpoint | Canonical evaluation is recorded in 003. |
| 002 | [YOLO26 vs YOLOE-26 prompt feasibility](experiments/002_yolo26_vs_yoloe26_prompt_feasibility/) | Interrupted | Baseline evaluation completed; prompt training stopped during epoch 9/50. No prompt-effect claim. |
| 003 | [Baseline error diagnostics](experiments/003_yolo26s_baseline_error_diagnostics/) | Completed | Corrected error decomposition and committed result tables. |
| 004 | [Component diagnosis attempt](experiments/004_yolo26s_component_diagnosis_attempt/) | Invalidated / partial | Split audit was informative; custom evaluator returned contradictory zero metrics and head ablation ran out of GPU memory. |
| 005 | [All-country YOLO26m benchmark](experiments/005_yolo26m_rdd2022_all_countries/) | Invalidated | Source/output mismatches and an interrupted training trace require a clean rerun. |
| 006 | [Semantic prototype feasibility](experiments/006_yolo26s_semantic_prototype_feasibility/) | Setup failed | Dependency conflict occurred before the experiment ran. No scientific result. |

See [JOURNAL.md](JOURNAL.md) for the decision log and provenance notes.

## Repository layout

```text
.
├── experiments/          # Numbered, self-contained research units
│   └── NNN_name/
│       ├── experiment.ipynb
│       ├── README.md
│       ├── results/      # Small, reviewable tables and manifests
│       └── checkpoints/  # Weights excluded from Git
├── notebooks/templates/  # Clean experiment templates
├── data/
│   ├── raw/              # Local source data excluded from Git
│   └── processed/        # Local derived data excluded from Git
├── artifacts/            # Large generated artifacts excluded from Git
├── scripts/               # Experiment creation and validation tools
├── tests/                 # Repository integrity tests
└── JOURNAL.md             # Chronological evidence and decision log
```

## Reproduce an experiment

1. Read the experiment README, including its status and known limitations.
2. Obtain the dataset and record its checksum and license locally in
   `data/README.md`.
3. Update the Colab/Drive paths in `experiment.ipynb`.
4. Run all cells in a fresh runtime and save the executed notebook in place.
5. Commit only compact CSV/JSON results; keep datasets, checkpoints, cached
   predictions, and large plots outside Git.
6. Update the experiment README and `JOURNAL.md` with the environment, seed,
   checkpoint lineage, result, anomaly, and next decision.
7. Validate the repository:

   ```bash
   python scripts/validate_repo.py
   python -m unittest discover -s tests
   ```

Create a new numbered experiment with:

```bash
python scripts/create_experiment.py "short experiment name"
```

## Research-integrity conventions

- A native framework metric is not mixed with a custom evaluator without an
  explicit consistency check.
- Interrupted or failed runs remain visible but do not support conclusions.
- Model, split, seed, package versions, hardware, and checkpoint lineage belong
  in every completed experiment record.
- Prompt experiments require plain, shuffled, and meaningless-prompt controls,
  plus matched-budget comparisons, before attributing a gain to semantics.
- Dataset files, model weights, credentials, and private Drive artifacts are
  never committed.
