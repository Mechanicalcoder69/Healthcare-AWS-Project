import pandas as pd
import random
import os
from faker import Faker
from config import *

fake = Faker("en_US")

def generate_preauth_los_rvw():

    los = pd.read_csv("output/PREAUTH_LOS.csv")

    review_types = ["Initial", "Concurrent", "Final"]
    review_status = ["Approved", "Denied", "Pending"]

    records = []

    for i, row in los.iterrows():

        records.append({

            "LOS_RVW_ID": f"LRV{i+1:08d}",
            "LOS_ID": row["LOS_ID"],
            "CASE_ID": row["CASE_ID"],
            "REVIEW_TYPE": random.choice(review_types),
            "REVIEW_STATUS": random.choice(review_status),
            "REVIEW_DATE": fake.date_between("-1y", "today"),
            "REVIEWER_NAME": fake.name()
        })

    df = pd.DataFrame(records)

    df.to_csv(
        os.path.join(OUTPUT_FOLDER, "PREAUTH_LOS_RVW.csv"),
        index=False
    )

    print(f"PREAUTH_LOS_RVW : {len(df):,} rows generated")