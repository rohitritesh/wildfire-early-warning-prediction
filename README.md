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

## Quickstart (Score Without Training)

1. Download the trained model (see **Model Download** below).
2. Prepare a small features CSV with these columns (one row per county×month):
   REGION_ID,YEAR,MONTH,PREV1_TOTAL,PREV3_TOTAL,P_LIGHTNING_3M,P_LARGE_3M
   CA | Los Angeles,2015,8,12,34,0.41,0.18
   CA | Orange,2015,8,5,11,0.20,0.09
3. 3. Install deps and score:
```bash
pip install -r requirements.txt
python scripts/score.py --model models/model_histgb_final.joblib --features data/sample_features.csv --out outputs/scored.csv

