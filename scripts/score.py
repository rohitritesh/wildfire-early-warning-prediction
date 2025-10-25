import argparse, joblib, pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="path to calibrated .joblib")
    ap.add_argument("--features", required=True, help="CSV with training-compatible columns")
    ap.add_argument("--out", default="scored.csv", help="output CSV")
    args = ap.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.features)
    # Expect columns: REGION_ID,YEAR,MONTH,PREV1_TOTAL,PREV3_TOTAL,P_LIGHTNING_3M,P_LARGE_3M
    feats_num = ["PREV1_TOTAL","PREV3_TOTAL","P_LIGHTNING_3M","P_LARGE_3M"]
    feats_cat = ["MONTH"]
    X = df[feats_num + feats_cat]
    df["RISK"] = model.predict_proba(X)[:,1]
    df.sort_values("RISK", ascending=False).to_csv(args.out, index=False)
    print(f"Saved → {args.out}")

if __name__ == "__main__":
    main()
