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

## Additional reported run results

The [run archive](records/README.md) records 12 model/configuration results
from [the supplied experiment log](runs%20%285%29%20%281%29.pdf), transcribed on
2026-11-04. The PDF is dated 2026-05-02; individual run dates are not reported.
These are **PDF-reported results**, with source-page references and training
settings preserved in CSV files. They have not been independently reproduced
and do not replace the canonical checkpoint evaluation above.

All values below are **test** metrics on a 0–1 scale. Dataset variants have
different splits and class counts; compare within a setup.

| Dataset | Model | Epochs / batch | Augmentation | mAP50 | mAP50–95 | Precision | Recall |
|---|---|---|---|---:|---:|---:|---:|
| China MotorBike, 4 classes | YOLO26m | 200 / 32 | Paper-style/default | 0.902 | 0.599 | 0.899 | 0.904 |
| China MotorBike, 4 classes | YOLO11m | 200 / 32 | Paper-style/default | 0.911 | 0.605 | 0.900 | 0.888 |
| China All, 5 classes | YOLO26s | 300 / 32 | Explicit settings | 0.848 | 0.569 | 0.850 | 0.811 |
| China All, 5 classes | YOLO8m | 300 / 32 | Explicit settings | 0.839 | 0.552 | 0.846 | 0.811 |
| China All, 5 classes | YOLO8s | 300 / 16 | Explicit settings | 0.856 | 0.545 | 0.867 | 0.813 |
| China All, 5 classes | YOLO26m | 300 / 16 | Explicit settings | 0.850 | 0.567 | 0.877 | 0.804 |
| All, 4 classes | YOLO26s | 100 / 32 | Disabled | 0.425 | 0.191 | 0.555 | 0.428 |
| All, 4 classes | YOLO26s | 100 / 16 | Default | 0.576 | 0.299 | 0.657 | 0.524 |
| All, 4 classes | YOLO8s | 100 / 16 | Default | 0.588 | 0.302 | 0.641 | 0.557 |
| Japan, 4 classes | YOLO26s | 100 / 32 | Disabled | 0.390 | 0.162 | 0.495 | 0.434 |
| Japan, 4 classes | YOLO26s | 100 / 16 | Default | 0.533 | 0.240 | 0.569 | 0.543 |
| Japan, 4 classes | YOLO8s | 100 / 16 | Default | 0.537 | 0.241 | 0.565 | 0.523 |

Model names `YOLO8s` and `YOLO8m` follow the PDF spelling. China All YOLO26s
also reports validation mAP50 **0.883**, mAP50–95 **0.597**, precision **0.864**,
and recall **0.837**. See the archive for per-class scores and full setup.
The disabled/default comparisons also change batch size and workers; Japan
additionally changes learning rate from 0.01 to 0.02. They do not isolate an
augmentation effect. Seeds, package versions, and checkpoint hashes are absent.

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
├── records/              # PDF-reported runs, CSV metrics, and provenance
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
