# US Wildfire Early Warning Prediction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/ROHITRITESH/wildfire-early-warning-prediction/blob/main/notebooks/wildfire_training_colab.ipynb)

**Summary.** AI-driven early warning for US wildfires at the **county × month** level.  
Trained on FPA-FOD (1992–2015) using time-aware validation and calibrated probabilities.

**Key results (held-out 2013–2015):**
- PR-AUC ≈ **0.78**
- Precision@Top-10% ≈ **0.92**
- Calibrated risks (isotonic)

## Repo layout
wildfire-early-warning/
├─ notebooks/
│ └─ wildfire_training_colab.ipynb
├─ scripts/
│ └─ score.py
├─ models/
│ └─ model_histgb_final.joblib
├─ outputs/
│ ├─ pr_curve_final.png
│ ├─ precision_at_10_final.png
│ └─ calibration_final.png
├─ data/
├─ requirements.txt
├─ README.md
└─ LICENSE
