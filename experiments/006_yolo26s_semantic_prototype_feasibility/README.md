# 006 — YOLO26s Semantic Prototype Feasibility

- **Status:** Setup failed; experiment not run
- **Intended hardware:** Colab T4
- **Models:** YOLO26s plus OpenCLIP ViT-B/32

## Goal

Test whether text prompts, train-set visual prototypes, or a lightweight
alignment adapter can improve semantic classification of RDD2022 damage crops
and matched YOLO detections.

## Intended controls

- Zero-shot prompt ensembles versus learned visual prototypes.
- Optional lightweight adapter on frozen image embeddings.
- Classification of ground-truth crops separately from matched detection
  boxes, avoiding confusion between localization and semantics.
- Per-class confusion matrices and a thin-crack subset analysis.

## Outcome

Only the dependency-installation cell ran. It upgraded pandas to 3.0.5, which
conflicted with the Colab and cuDF requirements shown in the output. No dataset
preparation, embedding extraction, model evaluation, or comparison ran.
Consequently, this notebook provides a research design but no scientific
result.

## Valid rerun requirements

Pin a Colab-compatible environment before installation, verify imports in a
fresh runtime, record the exact OpenCLIP weights and package versions, and then
run every cell in order. Report semantic-head feasibility only after comparison
with the strong classification-given-localization result from experiment 003.
