# 003 — YOLO26s Baseline Error Diagnostics

## Goal

Diagnose the trained experiment 001 baseline before selecting a custom YOLO26
architecture modification.

## Dependency

This analysis loads the best checkpoint from
[`001_yolo26s_rdd2022_baseline`](../001_yolo26s_rdd2022_baseline/). It performs
no training.

## Questions

1. Which classes are confused?
2. Which objects are missed?
3. Are thin or small objects the dominant weakness?
4. Are errors primarily classification, localization, or false positives?
5. Which intervention is justified by the evidence?

## Configuration

| Setting | Value |
|---|---|
| Dataset | RDD2022 China test split |
| Baseline model | YOLO26s from experiment 001 |
| Image size | 640 |
| Diagnostic prediction confidence | 0.05 |
| Matching IoU | 0.50 |
| Validation batch size | 8 |
| Prediction batch size | 4 |
| Hardware | Colab T4 |

## Results

| Diagnostic | Result |
|---|---:|
| Test objects | 893 |
| Official mAP50 | 0.8453 |
| Official mAP50–95 | 0.5802 |
| Official precision | 0.8563 |
| Official recall | 0.7992 |
| Localization recall at diagnostic threshold | 0.8701 |
| Correct-detection recall at diagnostic threshold | 0.8611 |
| Classification accuracy given localization | 0.9897 |
| High-aspect-ratio miss rate | 0.1155 |
| Small-object miss rate | 0.1228 |

### Geometry

High-aspect-ratio objects were not the dominant failure:

| Aspect-ratio bucket | Objects | Miss rate |
|---|---:|---:|
| AR < 2 | 235 | 0.1660 |
| AR 2–4 | 252 | 0.1190 |
| AR 4–8 | 293 | 0.1195 |
| AR ≥ 8 | 113 | 0.1062 |

The highest miss rate occurred for compact objects (`AR < 2`), not elongated
objects. Medium-area objects had a 0.1623 miss rate; the tiny bucket contained
only six objects and is too small for a strong conclusion.

### Classification and false-positive candidates

Only 8 of 777 localized objects were assigned the wrong class. The diagnostic
run retained predictions at confidence 0.05 and produced 728 unmatched
predictions, dominated by longitudinal (402) and transverse (216) crack
candidates.

These counts are useful for mining background errors, but they are not the
model's official false-positive rate: the deliberately low 0.05 threshold is
far below the operating point used for the official precision metric.

## Conclusion

The evidence does not justify prioritizing a thin-crack geometry adapter or a
semantic classification head. The next controlled experiment should first
analyze confidence calibration and hard negatives for crack-like background
textures, then test a targeted background-aware loss or hard-negative sampling
against the unchanged experiment 001 baseline.
