#!/usr/bin/env python3
"""RQ3 Bottleneck, Ablation, and Fusion

This lightweight entry point keeps the GitHub repository aligned with the paper's RQ structure.
Use run_extra_experiments_and_figures.py for bottleneck/ablation and run_final_three_experiments.py for final fusion/nested-beta diagnostics.
"""
from pathlib import Path

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    print("RQ3 Bottleneck, Ablation, and Fusion")
    print("Use run_extra_experiments_and_figures.py for bottleneck/ablation and run_final_three_experiments.py for final fusion/nested-beta diagnostics.")
    print("\nRecommended commands:")
    print("  python experiments/run_extra_experiments_and_figures.py")
    print("  python experiments/run_final_three_experiments.py")
    print("  python experiments/run_rq4_synthetic_second_order.py")
    print("  python visualization/run_tsne_embedding_visualization.py")
