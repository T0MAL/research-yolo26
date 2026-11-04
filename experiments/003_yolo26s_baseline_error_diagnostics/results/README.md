# Result manifest

These files were produced by the executed Colab notebook.

| File | Description |
|---|---|
| `official_metrics.csv` | Official overall and per-class Ultralytics metrics |
| `diagnostic_summary.csv` | One-row error summary |
| `per_class_error_decomposition.csv` | Correct, misclassified, missed, and unmatched counts |
| `matched_class_confusion_matrix.csv` | Confusion matrix for localized objects |
| `top_confusion_pairs.csv` | Ranked non-diagonal class confusions |
| `error_by_aspect_ratio.csv` | Localization and class-correct recall by geometry |
| `error_by_area.csv` | Localization and class-correct recall by object area |
| `false_positive_summary.csv` | Unmatched low-threshold predictions by class |

Not copied into Git:

- Cached per-image predictions
- Error visualization images
- Baseline checkpoint

Full Drive artifact location:
`/content/drive/MyDrive/Research/runs_rdd2022/yolo26s_baseline_diagnostics`
