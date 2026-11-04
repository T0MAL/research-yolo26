# 005 — YOLO26m RDD2022 All-Country Benchmark

- **Status:** Invalidated; clean rerun required
- **Intended model:** YOLO26m
- **Intended dataset:** RDD2022 all-country split
- **Observed accelerator:** NVIDIA L4

## Goal

Train a medium YOLO26 detector on an all-country RDD2022 split and compare it
with published road-damage baselines.

## Why no result is reported

The retained notebook is useful provenance but its source and stored outputs
are not internally consistent:

- Training output ends partway through epoch 37 of 100.
- Current source configures `yolo26m` and run name
  `yolov26m_rdd2022_ALL`, while a stored downstream output points to a
  `yolov26s_rdd2022_ALL` checkpoint. This indicates stale output from another
  notebook state or run.
- The title and comparison table still label the model as YOLOv8/YOLOv8s.
- The dataset inventory first reports `train/val/test`, but a later background
  audit scans `train_set/val_set/test_set` and therefore reports zero images.
- The markdown says 200 epochs while the training call uses 100.

Because output-to-source provenance cannot be established, the displayed
validation metrics are not treated as evidence and no CSV result is committed.

## Valid rerun requirements

The [PDF run archive](../../records/README.md), added on 2026-11-04, separately
reports All 4-class YOLO26s and YOLO8s results under `RUN-ALL-4C-001`. These do
not establish the lineage of this notebook's intended YOLO26m run, so its
invalidated status remains unchanged. The PDF's Full V1 YOLO26s/YOLO26m entry
appears only in its index and has no detailed result to recover.

1. Use one model name and one run directory throughout the notebook.
2. Detect and assert the actual split directory names before any audit.
3. Record dataset checksum, country composition, split policy, seed, package
   versions, and checkpoint checksum.
4. Restart the runtime, run all cells in order, and reject stale outputs.
5. Compare against papers only when dataset, classes, split, and evaluation
   protocol are genuinely matched.
