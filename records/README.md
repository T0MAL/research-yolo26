# Reported run records

Transcribed on **2026-11-04** from [runs (5) (1).pdf](../runs%20%285%29%20%281%29.pdf),
*RDD2022 + YOLO26 Experiment Database — Clean Experiment Log*. The document's
own last-updated date is **2026-05-02**; individual execution dates are absent.

**Status: reported in PDF.** These are 12 model/configuration records with 12
test results, one validation result, and 24 per-class results. Transcription
was checked against the PDF pages. Raw training logs, executed notebooks,
checkpoint hashes, seeds, and package versions were not supplied with these
records, so they are not independently reproduced results. No checkpoint
identity with experiments 001–006 is established.

## Files and conventions

| File | Contents |
|---|---|
| [datasets.csv](datasets.csv) | Four detailed dataset setups and one index-only entry; split sizes, classes, background counts, source paths, and cleaning notes. |
| [runs.csv](runs.csv) | Twelve configurations, including optimizer, batch, learning rate, augmentation, and reported hardware. |
| [metrics.csv](metrics.csv) | Twelve test rows and one validation row, with source pages and evaluation sizes. |
| [per_class_metrics.csv](per_class_metrics.csv) | Test mAP50–95 for four classes in each of six All/Japan configurations. |
| [provenance.json](provenance.json) | Source SHA-256, source date, import date, counts, and provenance limitations. |

Metrics use the source's 0–1 scale and three-decimal precision. Empty CSV fields
mean **not reported**, not zero. `epochs_as_reported` records the stated setup,
not independently verified completed epochs. `record_id` is a repository key;
`source_run_id` preserves the PDF's group label, which covers several models or
configurations. Model labels `YOLO8s` and `YOLO8m` are retained verbatim.

## Test results

| Dataset / source run ID | Model | Epochs | Batch | LR | Augmentation | mAP50 | mAP50–95 | Precision | Recall | PDF page |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| China MotorBike / RUN-CM-001 | YOLO26m | 200 | 32 | 0.01 | Paper-style/default | 0.902 | 0.599 | 0.899 | 0.904 | 3 |
| China MotorBike / RUN-CM-001 | YOLO11m | 200 | 32 | 0.01 | Paper-style/default | 0.911 | 0.605 | 0.900 | 0.888 | 3 |
| China All / RUN-CHINA-ALL-001 | YOLO26s | 300 | 32 | 0.01 | China explicit | 0.848 | 0.569 | 0.850 | 0.811 | 4 |
| China All / RUN-CHINA-ALL-001 | YOLO8m | 300 | 32 | 0.01 | China explicit | 0.839 | 0.552 | 0.846 | 0.811 | 4 |
| China All / RUN-CHINA-ALL-001 | YOLO8s | 300 | 16 | 0.01 | China explicit | 0.856 | 0.545 | 0.867 | 0.813 | 4 |
| China All / RUN-CHINA-ALL-001 | YOLO26m | 300 | 16 | 0.01 | China explicit | 0.850 | 0.567 | 0.877 | 0.804 | 4 |
| All 4-class / RUN-ALL-4C-001 | YOLO26s | 100 | 32 | 0.01 | Disabled | 0.425 | 0.191 | 0.555 | 0.428 | 5 |
| All 4-class / RUN-ALL-4C-001 | YOLO26s | 100 | 16 | 0.01 | Default | 0.576 | 0.299 | 0.657 | 0.524 | 5 |
| All 4-class / RUN-ALL-4C-001 | YOLO8s | 100 | 16 | 0.01 | Default | 0.588 | 0.302 | 0.641 | 0.557 | 5 |
| Japan / RUN-JAPAN-4C-001 | YOLO26s | 100 | 32 | 0.01 | Disabled | 0.390 | 0.162 | 0.495 | 0.434 | 6 |
| Japan / RUN-JAPAN-4C-001 | YOLO26s | 100 | 16 | 0.02 | Default | 0.533 | 0.240 | 0.569 | 0.543 | 6 |
| Japan / RUN-JAPAN-4C-001 | YOLO8s | 100 | 16 | 0.02 | Default | 0.537 | 0.241 | 0.565 | 0.523 | 7 |

China All YOLO26s also reports **validation** mAP50 **0.883**, mAP50–95
**0.597**, precision **0.864**, and recall **0.837** on page 4. This is stored
as a separate split in `metrics.csv`.

## Per-class test mAP50–95

| Dataset | Model / augmentation | Longitudinal crack | Transverse crack | Alligator crack | Pothole |
|---|---|---:|---:|---:|---:|
| All 4-class | YOLO26s / disabled | 0.212 | 0.171 | 0.264 | 0.117 |
| All 4-class | YOLO26s / default | 0.337 | 0.263 | 0.387 | 0.209 |
| All 4-class | YOLO8s / default | 0.333 | 0.271 | 0.382 | 0.221 |
| Japan | YOLO26s / disabled | 0.133 | 0.112 | 0.257 | 0.148 |
| Japan | YOLO26s / default | 0.222 | 0.152 | 0.334 | 0.253 |
| Japan | YOLO8s / default | 0.225 | 0.173 | 0.335 | 0.232 |

All 4-class test evaluations report **2,184 images / 5,172 instances**; Japan
reports **790 images / 1,661 instances**. China MotorBike has 242 test images
and China All has 438; instance counts are not given for either China setup.

## Training setup

All configurations report image size **640**, **SGD**, momentum **0.937**, and
weight decay **0.0005**. China All, All 4-class, and Japan report three warmup
epochs and disk caching. China All reports NVIDIA L4 and 16 workers. All and
Japan report AMP enabled, 16 workers for disabled augmentation, and 8 workers
for default augmentation. Only All 4-class explicitly reports label smoothing
**0.1**. Unreported settings remain empty in the CSV.

Augmentation profile names in `runs.csv` mean:

- `paper_style_default`: the MotorBike source says “paper-style/default YOLO
  augmentation”; individual parameters are not supplied.
- `china_explicit`: HSV enabled; translate 0.1, scale 0.5, fliplr 0.5, mosaic
  1.0; degrees, shear, perspective, flipud, mixup, and copy-paste disabled.
- `disabled`: HSV, translate, scale, fliplr, mosaic, degrees, shear,
  perspective, flipud, mixup, and copy-paste disabled.
- `default`: the source says default without enumerating parameters or a
  framework version; exact defaults cannot be reconstructed from this PDF.

## Interpretation and unresolved provenance

The reported YOLO26s default-augmentation configurations exceed the disabled
ones by 0.108 mAP50–95 on All 4-class and 0.078 on Japan. These are configuration
comparisons: batch size and workers also change, and Japan's learning rate
changes from 0.01 to 0.02. They do not isolate an augmentation effect.

Default-configuration YOLO8s exceeds YOLO26s by 0.003 mAP50–95 on All 4-class
and 0.001 on Japan. These single reported results have no repeat-run variance
or uncertainty estimate. Different datasets, class counts, and training
budgets should not be pooled into a single ranking.

The PDF index also lists `DB-RDD22-FULL-4C-V1`, but supplies no corresponding
detailed run section. Its dataset row is `index_only`; no metrics are inferred.
Embedded paper screenshots remain in the original PDF and are not imported
as local run results. The MotorBike paper excerpt mentions 2,477 images and a
6:1:1 split, while the local setup reports 1,450/242/242 (1,934 total); the
relationship between those inventories is not explained.

The China All YOLO26s test result (0.848 / 0.569) does not replace experiment
003's canonical checkpoint evaluation (0.8453 / 0.5802). Likewise, these All
4-class records do not resolve experiment 005's source/output mismatch. Before
linking any record to an existing checkpoint or making a paper comparison,
recover dataset and checkpoint hashes, split-generation details, seed,
environment, and executed training/evaluation logs.
