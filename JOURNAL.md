# Research Journal

This file is the experiment index and decision log. Status labels distinguish
completed evidence from exploratory, interrupted, and invalidated work.

## Experiment index

| ID | Date | Experiment | Status | Key result or decision |
|---:|:---:|---|---|---|
| 001 | Not recorded | [YOLO26s RDD2022 baseline](experiments/001_yolo26s_rdd2022_baseline/) | Completed checkpoint | Canonical corrected evaluation is recorded in 003. |
| 002 | Not recorded | [YOLO26 vs YOLOE-26 prompt feasibility](experiments/002_yolo26_vs_yoloe26_prompt_feasibility/) | Interrupted | Prompt training stopped in epoch 9/50; no semantic-effect result. |
| 003 | 2026-07-23 | [YOLO26s baseline error diagnostics](experiments/003_yolo26s_baseline_error_diagnostics/) | Completed | Thin geometry and class confusion were not dominant; investigate calibration and crack-like background candidates. |
| 004 | Not recorded | [YOLO26s component diagnosis attempt](experiments/004_yolo26s_component_diagnosis_attempt/) | Invalidated / partial | Split audit raised a leakage warning; custom metrics failed and head ablation ran out of memory. |
| 005 | Not recorded | [YOLO26m all-country benchmark](experiments/005_yolo26m_rdd2022_all_countries/) | Invalidated | Stale source/output mismatches prevent attribution of the stored metrics. |
| 006 | Not recorded | [YOLO26s semantic prototype feasibility](experiments/006_yolo26s_semantic_prototype_feasibility/) | Setup failed | Dependency conflict occurred before data or models were evaluated. |

---

## 001 — YOLO26s RDD2022 baseline

**Question:** What reference performance does YOLO26s achieve on the RDD2022
China subset, and are elongated boxes a prominent failure mode?

**Record:** A baseline checkpoint exists at the private Drive run location. The
clean notebook in experiment 001 is the reproduction protocol; the canonical
checkpoint evaluation and compact tables are stored in experiment 003.

**Canonical metrics:** mAP50 0.8453, mAP50–95 0.5802, precision 0.8563,
recall 0.7992.

**Decision:** Keep this checkpoint unchanged as the reference model. Treat a
fresh run of the experiment 001 notebook as an independent reproduction, not a
continuation of the original run.

---

## 002 — YOLO26 vs YOLOE-26 prompt feasibility

**Question:** Do correct rich prompts improve detection beyond changes caused
by YOLOE pretraining, architecture, or training budget?

**Record:** The baseline checkpoint re-evaluated successfully with the same
canonical metrics. Rich-prompt YOLOE training was interrupted during epoch 9
of 50. The prompt interventions, matched-budget control, paired McNemar test,
bootstrap interval, and efficiency comparison did not run.

**Decision:** No prompt-effect claim is supported. Resume only from a verified
checkpoint and retain plain, shuffled, nonsense, and matched-budget controls.

---

## 003 — YOLO26s baseline error diagnostics

**Question:** Are baseline errors driven mainly by class confusion, poor
localization of thin/small objects, or background candidates?

**Run record:** RDD2022 China test split; 893 objects; Colab T4; image size 640;
diagnostic confidence 0.05; match IoU 0.50.

| Metric | Value |
|---|---:|
| Official mAP50 | 0.8453 |
| Official mAP50–95 | 0.5802 |
| Official precision | 0.8563 |
| Official recall | 0.7992 |
| Localization recall at confidence 0.05 | 0.8701 |
| Correct-detection recall at confidence 0.05 | 0.8611 |
| Classification accuracy given localization | 0.9897 |
| High-aspect-ratio miss rate | 0.1155 |
| Small-object miss rate | 0.1228 |

**Interpretation:** AR >= 8 objects had a 10.62% miss rate versus 16.60% for
AR < 2, so elongated geometry was not the measured bottleneck. Only 1.03% of
localized objects had the wrong class. At the intentionally permissive 0.05
threshold, 728 predictions were unmatched, dominated by longitudinal- and
transverse-crack candidates. This is a mining pool, not an official
false-positive rate.

**Decision:** Measure calibration and precision/recall across thresholds,
inspect high-confidence background errors, and test hard-negative mining or a
background-aware loss only if that diagnosis persists.

---

## 004 — YOLO26s component diagnosis attempt

**Question:** Can split auditing, stratified error analysis, anchor coverage,
and head-branch ablation isolate a component-level weakness?

**Useful evidence:** The notebook verified the stock end-to-end head. A
perceptual-hash audit flagged possible cross-split near-duplicates (distance <=
6): 29.9% validation-to-train and 26.5% test-to-train. These are warning flags,
not confirmed duplicate rates.

**Failure:** Native evaluation reported mAP50–95 0.578 for this notebook's
separate checkpoint, but the custom evaluator returned zero everywhere. The
zero CSVs are marked invalid. The head ablation then exhausted T4 memory.

**Decision:** Resolve checkpoint lineage, validate prediction caches against
native output, require evaluator agreement, and use group-aware splits before
rerunning the component ablation.

---

## 005 — YOLO26m all-country benchmark

**Question:** How does a medium YOLO26 model perform on an all-country RDD2022
split under a paper-comparable protocol?

**Failure:** The training trace ends in epoch 37/100, current source specifies
YOLO26m while stored output references a YOLO26s run path, old YOLOv8 labels
remain, and one audit scans nonexistent split names. Output cannot be reliably
attributed to the current source.

**Decision:** Retain the notebook as provenance but report no metric. Rerun
from a cleared notebook after normalizing model, split, epoch, and run naming.

---

## 006 — YOLO26s semantic prototype feasibility

**Question:** Can OpenCLIP text or visual prototypes improve semantic decisions
on road-damage crops and matched detector boxes?

**Failure:** The install cell introduced a pandas version conflict with the
Colab/cuDF environment. No experimental section ran.

**Decision:** Pin a compatible environment and compare against experiment
003's 98.97% classification accuracy given localization before investing in a
semantic head.
