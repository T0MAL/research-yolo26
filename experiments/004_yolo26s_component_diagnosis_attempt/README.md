# 004 — YOLO26s Component Diagnosis Attempt

- **Status:** Invalidated / partial
- **Hardware:** Colab Tesla T4
- **Model:** Stock YOLO26s, 10.01M parameters
- **Dataset:** RDD2022 China subset

## Goal

Train or reuse a stock YOLO26s checkpoint, audit the dataset splits, localize
errors by object geometry and class, estimate anchor coverage, and compare the
one-to-one and one-to-many detection-head branches.

## What ran successfully

- The notebook verified that the loaded model used the stock end-to-end YOLO26
  detection head.
- Native Ultralytics evaluation on 438 test images and 893 objects reported
  mAP50 0.854 and mAP50–95 0.578 for the notebook's
  `yolo26s_base/yolo26s_base_fresh` checkpoint.
- The split audit flagged substantial perceptual similarity across splits. At
  a perceptual-hash distance of 6 or less, 29.9% of validation images and
  26.5% of test images had a training-set neighbor. This is a leakage warning,
  not proof that the images are duplicates; a group-aware split audit is
  required before using split differences as paper evidence.
- The geometry-only audit found no obvious anchor-coverage collapse for
  elongated objects. In the AR >= 8 group, 8.3% had zero stride-32 in-box
  anchors, while none had four or fewer total in-box anchors.

## Why the run is invalidated

The custom evaluator returned zero AP and 100% misses for every category,
contradicting the native evaluation above. The two committed `*_invalid.csv`
files preserve those outputs specifically as failed diagnostics and must not be
reported as model performance. The final head-branch ablation then failed with
a CUDA out-of-memory error while attempting to allocate another 5.35 GiB.

The native metric also belongs to a different checkpoint path from the
canonical baseline evaluated in experiment 003, so the two values should not
be treated as repeat measurements of the same weights.

## Valid rerun requirements

1. Freeze and checksum one checkpoint before all evaluations.
2. Assert that cached predictions contain detections and compare a sample
   against direct model output.
3. Require the custom overall AP to agree with native AP within a declared
   tolerance before running stratified metrics.
4. Clear models between head branches, lower inference batch size, and write
   each branch's predictions to disk before loading the next model.
5. Create group-aware splits using location or capture-sequence identifiers,
   then repeat the official baseline evaluation.

See [results/README.md](results/README.md) for the invalid-output manifest.
