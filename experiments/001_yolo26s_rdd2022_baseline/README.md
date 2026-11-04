# 001 — YOLO26s RDD2022 Baseline

**Status:** Completed checkpoint; canonical corrected evaluation is in
[experiment 003](../003_yolo26s_baseline_error_diagnostics/).

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
| mAP50 | 0.8453 |
| mAP50–95 | 0.5802 |
| Precision | 0.8563 |
| Recall | 0.7992 |

## Conclusion

The baseline is suitable as the unchanged reference for controlled follow-up
experiments. These values come from the checkpoint evaluation and corrected
error analysis in experiment 003; use that experiment's CSV files as the
canonical metric source. The notebook here is the cleaned reproduction
protocol and should be rerun from a fresh environment before claiming an
independent reproduction.

## Related reported runs

The [PDF run archive](../../records/README.md) includes a China All YOLO26s
configuration with 300 epochs and batch 32, reporting test mAP50 0.848 and
mAP50–95 0.569. Its checkpoint identity with this experiment is unverified;
those values remain a separate record and do not replace the canonical
evaluation above.
