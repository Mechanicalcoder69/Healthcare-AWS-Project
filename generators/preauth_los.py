from utils.file_loader import load_master_data
from faker import Faker
import pandas as pd
import random
import os
from config import *

fake = Faker("en_US")

def generate_preauth_los():

    cases = pd.read_csv("output/PREAUTH_CASE.csv")

    records = []

    for i, row in cases.iterrows():

        requested_days = random.randint(1, 15)

        if row["CASE_STATUS"] == "Approved":
            approved_days = random.randint(1, requested_days)

        elif row["CASE_STATUS"] == "Pending":
            approved_days = 0

        else:
            approved_days = 0

        admission = fake.date_between(
            start_date="-2y",
            end_date="today"
        )

        discharge = fake.date_between(
            start_date=admission,
            end_date="+20d"
        )

        records.append({

            "LOS_ID": f"LOS{i+1:08d}",

            "CASE_ID": row["CASE_ID"],

            "ADMISSION_DATE": admission,

            "EXPECTED_DISCHARGE_DATE": discharge,

            "REQUESTED_DAYS": requested_days,

            "APPROVED_DAYS": approved_days,

            "LOS_STATUS": row["CASE_STATUS"]

        })

    df = pd.DataFrame(records)

    df.to_csv(
        os.path.join(
            OUTPUT_FOLDER,
            "PREAUTH_LOS.csv"
        ),
        index=False
    )

    print(f"PREAUTH_LOS : {len(df):,} rows generated")