# 001 — YOLO26s RDD2022 Baseline

## Goal

Establish a YOLO26s baseline on the RDD2022 China subset and test whether
thin, elongated damage boxes are a prominent failure mode.

## Hypothesis

Recall will be lower for boxes with aspect ratio 8 or greater than for boxes
with aspect ratio below 2. The notebook also checks whether the one-to-one
NMS-free head loses accuracy relative to the one-to-many branch.

## Run

1. Open `experiment.ipynb` in Google Colab with a T4 GPU.
2. Check the Drive dataset and output paths in the setup cell.
3. Run all cells.
4. Save the executed notebook back to this directory.
5. Copy small CSV results from Drive into `results/`.
6. Fill in the tables below and update the root `JOURNAL.md`.

## Configuration

| Setting | Value |
|---|---|
| Model | `yolo26s` |
| Dataset | RDD2022 China subset |
| Image size | 640 |
| Epochs | 100 |
| Batch size | 16 |
| Optimizer | SGD |
| Seed | 0 |
| Intended hardware | Colab T4 |

## Expected result files

- `official_metrics.csv`
- `recall_by_ar.csv`
- `recall_by_class.csv`
- `head_comparison.csv`
- `predictions_test.csv` (potentially large; do not commit if so)

See [`results/README.md`](results/README.md) for the result manifest.

## Result summary

| Metric | Value |
|---|---:|
| mAP50 | Pending |
| mAP50–95 | Pending |
| Precision | Pending |
| Recall | Pending |

## Conclusion

Pending execution.
