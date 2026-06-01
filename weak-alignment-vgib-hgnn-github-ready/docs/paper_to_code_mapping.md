# Paper-to-Code Mapping

| Paper evidence | Purpose | Primary script | Expected outputs |
|---|---|---|---|
| RQ1 Primary Screening Performance | Compare VGIB-HGNN-Focal against tabular, neural, and graph baselines | `experiments/run_extra_experiments_and_figures.py` | Main performance CSVs, OOF predictions |
| RQ2 Weak Alignment Diagnostics | Cross-modal predictability, CCA, neighborhood overlap, risk-marker discordance | `experiments/run_extra_experiments_and_figures.py` | Weak-alignment tables and figures |
| RQ3 Bottleneck, Ablation, Fusion | Beta sensitivity, ablation, threshold-matched comparison, fusion diagnostics | `experiments/run_extra_experiments_and_figures.py`, `experiments/run_final_three_experiments.py` | Beta sensitivity, ablation, fusion CSVs |
| RQ4 Controlled Relational Benchmark | Synthetic second-order graph-position recovery | `experiments/run_rq4_synthetic_second_order.py` | Synthetic benchmark metrics and leakage diagnostics |
| RQ5 Deployment Diagnostic | Inductive patient insertion | `experiments/run_extra_experiments_and_figures.py` | Inductive/transductive comparison |
| RQ6 Boundary Cases and Interpretability | Graph-specific boundary subgroup contribution and t-SNE | `experiments/run_final_three_experiments.py`, `visualization/run_tsne_embedding_visualization.py` | Subgroup tables, t-SNE coordinates, figures |
