# Reproducibility Notes

This repository follows the paper's leakage-aware evaluation principle.

## Fold-safe operations

The following operations should be fitted or selected using training data only whenever they affect model fitting or operating-point selection:

- missing-value imputation
- feature scaling
- microbiome prevalence filtering
- species selection
- patient--species graph construction
- beta selection
- threshold selection

## Metrics

The screening task emphasizes:

- Risk Recall
- Risk Precision
- Risk F1
- PR-AUC
- AUC
- Macro-F1

Risk Recall and Risk F1 are operating-point metrics and are sensitive to threshold selection. Thresholds should be selected from training or validation predictions only.

## Interpretation

The graph branch should be interpreted as complementary risk evidence under weak alignment, not as a universal replacement for strong patient-level predictors.
