#!/usr/bin/env python3
"""RQ6 Boundary Cases and Interpretability

This lightweight entry point keeps the GitHub repository aligned with the paper's RQ structure.
Boundary subgroup contribution is implemented in run_final_three_experiments.py; t-SNE visualization is in visualization/run_tsne_embedding_visualization.py.
"""
from pathlib import Path

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    print("RQ6 Boundary Cases and Interpretability")
    print("Boundary subgroup contribution is implemented in run_final_three_experiments.py; t-SNE visualization is in visualization/run_tsne_embedding_visualization.py.")
    print("\nRecommended commands:")
    print("  python experiments/run_extra_experiments_and_figures.py")
    print("  python experiments/run_final_three_experiments.py")
    print("  python experiments/run_rq4_synthetic_second_order.py")
    print("  python visualization/run_tsne_embedding_visualization.py")
