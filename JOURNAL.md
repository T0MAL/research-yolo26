# Research Journal

This is the experiment index and decision log. Update it after every run,
including failed or interrupted runs.

## Experiment index

| ID | Date | Experiment | Hypothesis | Status | Key result |
|---:|:---:|---|---|---|---|
| 001 | — | [YOLO26s RDD2022 baseline](experiments/001_yolo26s_rdd2022_baseline/) | Establish a reproducible baseline and identify whether elongated cracks are a major failure mode. | Ready to run | Pending |
| 002 | — | [YOLO26 vs YOLOE-26 prompt feasibility](experiments/002_yolo26_vs_yoloe26_prompt_feasibility/) | Correct semantic prompts improve detection beyond architecture or training-budget effects. | Ready to run | Pending |

Status values: `planned`, `ready to run`, `running`, `completed`, `failed`,
or `superseded`.

---

## 001 — YOLO26s RDD2022 baseline

**Date:** Not run yet  
**Notebook:** [`experiments/001_yolo26s_rdd2022_baseline/experiment.ipynb`](experiments/001_yolo26s_rdd2022_baseline/experiment.ipynb)  
**Status:** Ready to run

### Question

What baseline performance does YOLO26s achieve on the RDD2022 China subset,
and does recall degrade for high-aspect-ratio road damage?

### Planned comparisons

- Overall and per-class test metrics.
- Recall grouped by ground-truth box aspect ratio.
- One-to-one (NMS-free) versus one-to-many (+NMS) detection heads.

### Run record

- Dataset version/checksum:
- Train/validation/test split:
- Git commit:
- Colab runtime/GPU:
- Python, PyTorch, Ultralytics versions:
- Random seed:
- Start/end time:

### Results

| Metric | Value |
|---|---:|
| mAP50 | Pending |
| mAP50–95 | Pending |
| Precision | Pending |
| Recall | Pending |

### Interpretation and next decision

Pending execution. Add links to result CSVs, note anomalies or failures, and
state the single next experiment justified by the evidence.

---

## 002 — YOLO26 vs YOLOE-26 prompt feasibility

**Date:** Not run yet  
**Notebook:** [`experiments/002_yolo26_vs_yoloe26_prompt_feasibility/experiment.ipynb`](experiments/002_yolo26_vs_yoloe26_prompt_feasibility/experiment.ipynb)  
**Status:** Ready to run  
**Depends on:** Experiment 001 baseline checkpoint

### Question

Does YOLOE-26 obtain a genuine semantic benefit from rich road-damage prompts,
or do apparent gains arise from architecture, pretraining, or extra training?

### Planned comparisons

- Existing YOLO26s baseline versus rich-prompt YOLOE-26s.
- Correct rich prompts versus plain names, shuffled prompts, and nonsense.
- Optional matched-budget YOLO26 and plain-prompt-training controls.
- Per-class and aspect-ratio recall.
- Model size, GFLOPs, T4 latency, and peak memory.
- Paired McNemar test and bootstrap confidence interval.

### Run record

- Dataset version/checksum:
- Baseline checkpoint:
- Git commit:
- Colab runtime/GPU:
- Python, PyTorch, Ultralytics versions:
- Random seed:
- Optional controls enabled:
- Start/end time:

### Results

| Metric | YOLO26s baseline | YOLOE-26s rich prompts | Difference |
|---|---:|---:|---:|
| mAP50 | Pending | Pending | Pending |
| mAP50–95 | Pending | Pending | Pending |
| Paired recall | Pending | Pending | Pending |
| T4 latency (ms/image) | Pending | Pending | Pending |

### Interpretation and next decision

Pending execution. Do not attribute improvement to prompt semantics unless
correct prompts outperform both shuffled and meaningless controls. Record
whether the paired confidence interval excludes zero and whether the efficiency
cost is acceptable.
