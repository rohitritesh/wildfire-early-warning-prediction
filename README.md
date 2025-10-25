# US Wildfire Early Warning Prediction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/ROHITRITESH/wildfire-early-warning-prediction/blob/main/notebooks/wildfire_training_colab.ipynb)

**Summary:** This repository delivers a practical, reproducible pipeline for **early warning of US wildfires at the county × month level**. Using the publicly available US Wildfires dataset (1992–2015), I aggregate incident records into a complete county–month panel, engineer **lagged signals** (last 1 month and last 3 months of activity, lightning share, and large-fire share), and learn a probability of **any wildfire next month**. Two complementary models, a calibrated **Logistic Regression** and a tuned, calibrated **Histogram Gradient Boosting** model, are trained with **time-aware validation** to avoid leakage. Probabilities are **calibrated via isotonic regression**, so a predicted 0.70 corresponds closely to a 70% observed frequency which is useful for operations and communication.

**Headline performance on held-out 2013–2015:** PR-AUC ≈ **0.78**, Precision@Top-10% ≈ **0.92**, with good calibration. The repository includes a one-click Colab notebook for full training and a minimal **`scripts/score.py`** so anyone can score **future months** provided the same input features are supplied. This design keeps deployment simple wherein agencies can compute rolling features from their latest logs and obtain risk rankings immediately. Limitations are noted (monthly granularity, need for minimal history, potential reporting bias), and the approach is extensible to weather/vegetation covariates.


**Key results (held-out 2013–2015):**
- PR-AUC ≈ **0.78**
- Precision@Top-10% ≈ **0.92**
- Calibrated risks (isotonic)

## Repo layout
```
wildfire-early-warning-prediction/
├─ notebooks/
│  └─ wildfire_training_colab.ipynb
├─ scripts/
│  └─ score.py
├─ models/
│  └─ model_histgb_final.joblib       
├─ outputs/
│  ├─ pr_curve_final.png
│  ├─ precision_at_10_final.png
│  └─ calibration_final.png
├─ data/
│  └─ sample_features.csv            
├─ requirements.txt
├─ .gitignore
├─ README.md
└─ LICENSE
```
## Data Source

U.S. Wildfires, 1992–2015 [(Kaggle mirror)](https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires).  
Please obtain the dataset and place `FPA_FOD_20170508.sqlite` locally for training.

## Model Download

The `.joblib` file is committed under `models/`.

## Quickstart (Score Without Training)

1. Download the trained model (see **Model Download** below).
2. Prepare a small features CSV with these columns (one row per county×month):
      ```csv
   REGION_ID,YEAR,MONTH,PREV1_TOTAL,PREV3_TOTAL,P_LIGHTNING_3M,P_LARGE_3M
   CA | Los Angeles,2015,8,12,34,0.41,0.18
   CA | Orange,2015,8,5,11,0.20,0.09
3. Save it as data/sample_features.csv
4. Install and run the scorer:
   ```bash
   python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   mkdir -p outputs
   python scripts/score.py --model models/model_histgb_final.joblib --features data/sample_features.csv --out outputs/scored.csv
   ```
5. What you get:
   A ranked CSV at outputs/scored.csv with a new RISK column (higher = higher wildfire risk).

## Model Card & Limitations

**Use:** Prioritise county×month wildfire risk for early warning.  
**Features:** last-month and last-3-months incident counts and proportions.  
**Models:** Logistic Regression; Histogram Gradient Boosting (tuned, calibrated).  
**Limits:** Monthly granularity; requires minimal recent history; historical reporting bias possible.

## Licence
MIT License. See `LICENSE`.
