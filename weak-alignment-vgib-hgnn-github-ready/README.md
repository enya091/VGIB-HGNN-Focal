# Weak-Alignment VGIB-HGNN

This repository contains the code release for:

**Uncertainty-Aware Entity-Anchored Graph Mining for Weakly Aligned Cognitive Risk Stratification**

The project studies early cognitive risk screening under weakly aligned brain MRI and gut microbiome modalities. The main model represents demographic and brain ROI variables as patient-node attributes, promotes microbiome species into entity nodes in a patient--species heterogeneous graph, and applies a variational graph information bottleneck (VGIB) with a focal risk objective.

## Repository layout

```text
configs/                 Experiment configuration templates
data/                    Placeholder for private biomedical data
docs/                    Paper-to-code mapping and reproducibility notes
experiments/             Executable experiment scripts
visualization/           Qualitative t-SNE embedding visualization
legacy_colab_exports/    Original unmodified Colab-exported scripts
src/                     Modular placeholders for future refactoring
outputs/                 Generated result tables and figures
```

## Data

Raw data are not included because the cohort contains biomedical and demographic information.

Place the following files under `data/` before running real-cohort experiments:

```text
data/data.csv
data/micro.csv
data/all_brain_result_1(3).csv
```

The binary screening task uses:

```text
Normal = 0
MCI or Dementia = 1
```

## Installation

```bash
pip install -r requirements.txt
```

For PyTorch Geometric, install the wheel compatible with your PyTorch/CUDA environment if the standard installation fails.

## Recommended run order

### 1. Main and reviewer-facing real-cohort experiments

```bash
python experiments/run_extra_experiments_and_figures.py
```

This consolidated script contains the main tuned VGIB-HGNN experiment suite and additional reviewer-facing analyses, including weak-alignment diagnostics, bottleneck sensitivity, topology controls, inductive insertion, and stronger baselines.

### 2. Final supplementary experiments

```bash
python experiments/run_final_three_experiments.py
```

This script runs the final three supplementary analyses: auxiliary/gated fusion, nested beta selection, and boundary subgroup contribution.

### 3. RQ4 synthetic second-order graph-position benchmark

```bash
python experiments/run_rq4_synthetic_second_order.py
```

This script runs the controlled relational benchmark for second-order graph-position signal recovery.

### 4. Qualitative t-SNE visualization

```bash
python visualization/run_tsne_embedding_visualization.py
```

The t-SNE visualization is intended for qualitative interpretation and diagnostics only. It should not be used as the primary performance estimate.

## Paper-to-code mapping

See [`docs/paper_to_code_mapping.md`](docs/paper_to_code_mapping.md).

## Reproducibility notes

The paper emphasizes leakage-aware evaluation. Any preprocessing step that affects model fitting or operating-point selection should be performed within training folds, including imputation, scaling, species filtering, species selection, graph construction, beta selection, and threshold selection.

See [`docs/reproducibility_notes.md`](docs/reproducibility_notes.md).

## Legacy scripts

The original Colab-exported scripts are preserved under `legacy_colab_exports/` for auditability. The cleaned GitHub-friendly copies under `experiments/` and `visualization/` remove Colab-only shell commands and download calls.
