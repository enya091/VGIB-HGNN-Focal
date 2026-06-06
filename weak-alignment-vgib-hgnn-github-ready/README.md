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

## Reproducing Paper Tables and Figures

The table below maps each major paper result to the corresponding script. Real-cohort experiments require the private biomedical cohort files listed in the Data section. The synthetic relational benchmark can be executed without access to the private cohort data.

| Paper item          | Description                                      | Command                                                                                                           | Expected output                                                       |
| ------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Table IV            | Primary screening performance                    | `python experiments/run_extra_experiments_and_figures.py`                                                         | Primary real-cohort screening metrics                                 |
| Fig. 2              | Weak-alignment diagnostics                       | `python experiments/run_extra_experiments_and_figures.py`                                                         | Cross-modal predictability, CCA, and neighborhood-overlap diagnostics |
| Fig. 3              | Bottleneck sensitivity and nested beta selection | `python experiments/run_extra_experiments_and_figures.py` and `python experiments/run_final_three_experiments.py` | Beta-sensitivity and nested-validation summaries                      |
| Table V             | Auxiliary fusion and strong-baseline diagnostics | `python experiments/run_final_three_experiments.py`                                                               | Fusion and baseline comparison tables                                 |
| Table VI            | Feature and relation ablation                    | `python experiments/run_extra_experiments_and_figures.py`                                                         | Controlled ablation results                                           |
| Table VII / Fig. 4  | Graph-only boundary subgroup contribution        | `python experiments/run_final_three_experiments.py`                                                               | Boundary subgroup gain table and figure                               |
| Table X             | Controlled graph-position benchmark              | `python experiments/run_rq4_synthetic_second_order.py`                                                            | Synthetic relational benchmark results                                |
| Table XI            | Inductive patient-insertion diagnostic           | `python experiments/run_extra_experiments_and_figures.py`                                                         | Inductive insertion results                                           |
| Table XII           | Empirical runtime                                | `python experiments/run_extra_experiments_and_figures.py`                                                         | Average end-to-end runtime summary                                    |
| t-SNE visualization | Qualitative embedding diagnostic                 | `python visualization/run_tsne_embedding_visualization.py`                                                        | Pre-bottleneck and VGIB latent-space visualizations                   |

## Main Hyperparameters and Evaluation Protocol

Unless otherwise stated, real-cohort results are computed using leakage-aware out-of-fold evaluation. Preprocessing, imputation, scaling, species filtering, graph construction, beta selection, and threshold selection are performed within the training or validation portion of each fold. Held-out labels are not used for threshold selection.

The main VGIB-HGNN-Focal configuration uses a two-layer heterogeneous graph encoder, hidden dimension 64, latent dimension 32, two attention heads, focal-loss focusing parameter gamma = 1.0, and a validation-selected or pre-specified bottleneck coefficient beta depending on the experiment. The primary configuration reports beta = 1e-4, while sensitivity and nested-validation experiments evaluate beta values in the candidate set reported in the paper.

The real cohort contains 454 subjects after multimodal matching, including 346 Normal subjects and 108 high-risk subjects, where MCI and Dementia are merged into the positive screening class. The private biomedical cohort cannot be redistributed because it contains demographic and medical information. For this reason, the repository provides code, configuration templates, documentation, and synthetic benchmark scripts, but not the raw real-cohort data.

## Reproducibility Checklist Notes

* Dependencies are specified in `requirements.txt`.
* Training and evaluation scripts are provided under `experiments/`.
* Qualitative visualization scripts are provided under `visualization/`.
* Real-cohort raw data are not included due to privacy and ethics constraints.
* No pretrained model checkpoint is released because the paper reports cross-validation and fold-specific models rather than a single deployment checkpoint.
* The synthetic relational benchmark can be run without private data and is included to reproduce the controlled graph-position recovery experiment.
