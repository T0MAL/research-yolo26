# 002 — YOLO26 vs YOLOE-26 Prompt Feasibility

**Status:** Interrupted during rich-prompt training at epoch 9 of 50. The
notebook retains the partial execution trace, but no prompt-model result or
semantic-effect conclusion was produced.

## Goal

Determine whether an in-model vision-language prompt head provides a genuine
semantic benefit for RDD2022-China road-damage detection before investing in a
new lightweight prompt-aware architecture.

## Dependency

This experiment uses the trained checkpoint from
[`001_yolo26s_rdd2022_baseline`](../001_yolo26s_rdd2022_baseline/) as its
reference model. Run experiment 001 first and confirm that `BASELINE_CKPT` in
the notebook points to its Drive checkpoint.

## Hypothesis

A useful prompt-aware detector should:

- outperform the existing YOLO26s baseline;
- perform better with correct rich prompts than with plain, shuffled, or
  meaningless prompts;
- show a paired recall improvement whose confidence interval excludes zero;
- retain acceptable T4 latency, memory use, and model size.

## Controlled comparisons

The primary run compares the existing YOLO26s baseline with one trained
YOLOE-26s checkpoint evaluated under four prompt interventions:

1. Correct rich road-damage descriptions.
2. Plain class names.
3. Shuffled incorrect descriptions.
4. Meaningless control prompts.

For a stronger paper ablation, enable the matched-budget YOLO26 and
plain-prompt-training controls in the notebook.

## Configuration

| Setting | Value |
|---|---|
| Baseline experiment | 001 |
| Dataset | RDD2022 China subset |
| Prompt model | YOLOE-26s |
| Image size | 640 |
| Prompt-training epochs | 50 |
| Training batch size | 8 |
| Seed | 0 |
| Intended hardware | Colab T4 |
| Paired confidence threshold | 0.25 |
| Paired IoU threshold | 0.50 |
| Bootstrap samples | 5,000 |

## Run

1. Open `experiment.ipynb` in a Colab T4 runtime.
2. Verify the dataset zip, baseline checkpoint, and output Drive paths.
3. Run all cells. Enable optional controls when runtime permits.
4. Save the executed notebook back to this directory.
5. Copy the compact CSV outputs into `results/`.
6. Complete the result summary and update the root `JOURNAL.md`.

## Result summary

| Metric | YOLO26s baseline | YOLOE-26s rich prompts | Difference |
|---|---:|---:|---:|
| mAP50 | Pending | Pending | Pending |
| mAP50–95 | Pending | Pending | Pending |
| Paired recall | Pending | Pending | Pending |
| T4 latency (ms/image) | Pending | Pending | Pending |

### Completed before interruption

The baseline checkpoint was successfully re-evaluated:

| Metric | YOLO26s baseline |
|---|---:|
| mAP50 | 0.8453 |
| mAP50–95 | 0.5802 |
| Precision | 0.8563 |
| Recall | 0.7992 |

## Decision

No decision can be made from this run. Resume or restart training, then execute
the correct/plain/shuffled/nonsense prompt controls, matched-budget control,
paired statistics, and efficiency measurements before treating the direction
as supported.
