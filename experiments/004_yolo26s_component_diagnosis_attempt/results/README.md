# Result manifest

These files are retained as debugging provenance, not scientific results.

| File | Status | Reason |
|---|---|---|
| `overall_metrics_invalid.csv` | Invalid | All metrics are zero and contradict native mAP50–95 of 0.578. |
| `aspect_ratio_metrics_invalid.csv` | Invalid | Every bucket is zero because the upstream custom evaluation failed. |

The split-audit plots, prediction caches, gallery, and checkpoint remain in the
private experiment artifact location and are not committed.

