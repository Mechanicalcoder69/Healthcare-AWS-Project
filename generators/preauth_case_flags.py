import pandas as pd
import random
import os
from config import *

def generate_preauth_case_flags():

    cases = pd.read_csv("output/PREAUTH_CASE.csv")

    records = []

    for i, row in cases.iterrows():

        records.append({

            "FLAG_ID": f"FLG{i+1:08d}",

            "CASE_ID": row["CASE_ID"],

            "URGENT_FLAG": random.choices(
                ["Y", "N"],
                weights=[20, 80]
            )[0],

            "HIGH_COST_FLAG": random.choices(
                ["Y", "N"],
                weights=[10, 90]
            )[0],

            "CLINICAL_REVIEW_FLAG": random.choices(
                ["Y", "N"],
                weights=[30, 70]
            )[0],

            "FRAUD_FLAG": random.choices(
                ["Y", "N"],
                weights=[2, 98]
            )[0],

            "OUT_OF_NETWORK_FLAG": random.choices(
                ["Y", "N"],
                weights=[15, 85]
            )[0]

        })

    df = pd.DataFrame(records)

    df.to_csv(
        os.path.join(
            OUTPUT_FOLDER,
            "PREAUTH_CASE_FLAGS.csv"
        ),
        index=False
    )

    print(f"PREAUTH_CASE_FLAGS : {len(df):,} rows generated")