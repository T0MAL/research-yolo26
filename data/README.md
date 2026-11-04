# Data

`raw/` is for immutable source data and `processed/` is for generated,
training-ready data. Their contents are ignored by Git.

Document each dataset's source URL, license, download date, version/checksum,
class mapping, and split-generation procedure here or in a dataset-specific
README. Never place credentials or private download tokens in this repository.

## Dataset variants referenced by the experiments

| Variant | Observed split sizes | Classes | Used by |
|---|---|---|---|
| RDD2022 China subset | 3,502 train / 438 validation / 438 test images | longitudinal crack, transverse crack, alligator crack, pothole, repair | 001–004, 006 |
| RDD2022 all-country working split | 15,294 train / 4,370 validation / 2,184 test images | four classes reported by the notebook | 005 |

The counts above are execution-record observations, not a substitute for a
dataset manifest. Before the next run, add the archive checksum, authoritative
source and license, country composition, split-generation code, and any image
group identifiers. Experiment 004's perceptual-hash audit raised a possible
cross-split similarity concern, so a location- or sequence-aware split should
be considered before reporting final benchmark results.

## Dataset setups in the reported run archive

The [PDF-reported records](../records/README.md), imported on 2026-11-04,
preserve these additional dataset identifiers. Counts are transcribed from
the local setup descriptions, not from embedded paper excerpts.

| Dataset ID | Variant | Train / validation / test images | Classes | Background images (train / validation / test) |
|---|---|---|---:|---|
| DB-RDD22-CM-4C-V1 | China MotorBike | 1,450 / 242 / 242 | 4 | Not reported |
| DB-RDD22-CHINA-ALL-5C-V1 | China MotorBike + China Drone | 3,502 / 438 / 438 | 5 | 5 / 0 / 0 |
| DB-RDD22-ALL-4C-V2 | Prepared RDD2022 All | 15,294 / 4,370 / 2,184 | 4 | 0 / 0 / 0 |
| DB-RDD22-JAPAN-4C-V2 | Japan | 5,530 / 1,580 / 790 | 4 | Not reported / not reported / 0 |
| DB-RDD22-FULL-4C-V1 | Full RDD2022; index only | Not reported | 4 | Not reported |

The four classes are longitudinal crack, transverse crack, alligator crack,
and pothole; China All adds repair. Background is not a separate class.
The All test split reports 5,172 instances; Japan reports 1,661. Archive and
extraction paths, cleaning notes, and source pages are in
[datasets.csv](../records/datasets.csv).

Identical split counts do not establish identical image membership or
checkpoint lineage with the numbered experiments. The PDF does not supply
archive checksums, split seeds, or split-generation code. Its MotorBike paper
excerpt mentions 2,477 images, while the local run's split totals 1,934; that
relationship remains unresolved. The index-only Full V1 entry is not merged
with the detailed All V2 setup.
