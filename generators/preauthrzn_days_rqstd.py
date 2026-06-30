import pandas as pd
import random
import os
from config import *

def generate_preauthrzn_days_rqstd():

    los = pd.read_csv("output/PREAUTH_LOS.csv")

    records = []

    for i, row in los.iterrows():

        requested_days = int(row["REQUESTED_DAYS"])
        approved_days = int(row["APPROVED_DAYS"])

        records.append({

            "AUTH_DAY_ID": f"ADY{i+1:08d}",

            "LOS_ID": row["LOS_ID"],

            "CASE_ID": row["CASE_ID"],

            "REQUESTED_DAYS": requested_days,

            "APPROVED_DAYS": approved_days,

            "DENIED_DAYS": max(0, requested_days - approved_days),

            "EXTENSION_REQUIRED": "Y" if requested_days > 7 else "N"

        })

    df = pd.DataFrame(records)

    df.to_csv(
        os.path.join(
            OUTPUT_FOLDER,
            "PREAUTHRZN_DAYS_RQSTD.csv"
        ),
        index=False
    )

    print(f"PREAUTHRZN_DAYS_RQSTD : {len(df):,} rows generated")