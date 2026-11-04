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
